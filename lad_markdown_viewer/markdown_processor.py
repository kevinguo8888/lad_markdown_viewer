"""
核心Markdown处理模块
"""
import mistune
from mistune.plugins.formatting import strikethrough
from mistune.plugins.table import table
from mistune.plugins.task_lists import task_lists
import re
import unicodedata
import html as html_module

from .markdown_utils import extract_mermaid_blocks, restore_mermaid_blocks, slugify

class TocRenderer(mistune.HTMLRenderer):
    """自定义渲染器，为标题添加ID。"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.toc_items = []

    def heading(self, text, level):
        slug = slugify(text)
        self.toc_items.append((level, slug, text))
        return f'<h{level} id="{slug}">{text}</h{level}>\n'

def process_yaml_front_matter(md_text):
    """处理YAML front matter，将其转换为表格格式。"""
    yaml_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.search(yaml_pattern, md_text, re.DOTALL)
    if match:
        yaml_content = match.group(1)
        md_text = re.sub(yaml_pattern, '', md_text, count=1, flags=re.DOTALL)
        table_rows = []
        for line in yaml_content.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                table_rows.append(f"| {key} | {value} |")
        if table_rows:
            table_html = "## 文档元信息\n\n| 字段 | 值 |\n|------|----|\n"
            table_html += '\n'.join(table_rows)
            table_html += '\n\n'
            md_text = table_html + md_text
    return md_text

def render_markdown_to_html(md_text):
    """
    将完整的Markdown文本渲染为HTML。
    这是一个集中的处理流程，包括YAML、Mermaid和TOC。
    """
    # 1. 处理YAML元信息
    processed_md = process_yaml_front_matter(md_text)
    
    # 2. 提取Mermaid图表块
    processed_md, mermaid_blocks = extract_mermaid_blocks(processed_md)
    
    # 3. 使用自定义渲染器和插件来渲染Markdown
    renderer = TocRenderer()
    markdown = mistune.Markdown(renderer=renderer, plugins=[strikethrough, table, task_lists])
    html_body = markdown(processed_md)
    
    # 4. 解码HTML实体并恢复Mermaid图表块
    html_body = html_module.unescape(html_body)
    html_body = restore_mermaid_blocks(html_body, mermaid_blocks)
    
    return html_body 

def render_markdown_with_zoom(md_text):
    """
    渲染Markdown为HTML，并自动注入图片和Mermaid图的放大缩小控件、自动居中、留白等前端交互体验。
    """
    html_body = render_markdown_to_html(md_text)
    zoom_js_css = '''
    <style>
    .markdown-body img, .markdown-body .mermaid { cursor: zoom-in; transition: box-shadow 0.2s; }
    .markdown-body .mermaid, .markdown-body img { display: block; margin: 32px auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 12px rgba(0,0,0,0.06); padding: 24px; }
    .zoom-controls {
        position: absolute;
        right: 16px;
        top: 16px;
        z-index: 10001;
        display: flex;
        flex-direction: row;
        gap: 8px;
    }
    .zoom-btn {
        background: #fff;
        border: 1px solid #ccc;
        border-radius: 4px;
        width: 32px;
        height: 32px;
        font-size: 18px;
        cursor: pointer;
        box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        transition: background 0.2s;
    }
    .zoom-btn:hover { background: #f6f8fa; }
    .zoom-overlay {
        position: fixed;
        left: 0; top: 0; width: 100vw; height: 100vh;
        background: rgba(0,0,0,0.7);
        display: flex; align-items: center; justify-content: center;
        z-index: 9999;
        cursor: zoom-out;
        overflow: hidden;
    }
    </style>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        function createZoomOverlay(contentElem) {
            let overlay = document.createElement('div');
            overlay.className = 'zoom-overlay';
            let container = document.createElement('div');
            container.style.position = 'relative';
            container.style.display = 'inline-block';
            // 缩放控件
            let controls = document.createElement('div');
            controls.className = 'zoom-controls';
            let btnPlus = document.createElement('button');
            btnPlus.className = 'zoom-btn'; btnPlus.textContent = '+';
            let btnMinus = document.createElement('button');
            btnMinus.className = 'zoom-btn'; btnMinus.textContent = '-';
            let btnReset = document.createElement('button');
            btnReset.className = 'zoom-btn'; btnReset.textContent = '重置';
            controls.appendChild(btnPlus);
            controls.appendChild(btnMinus);
            controls.appendChild(btnReset);
            let scale = 1;
            let panX = 0, panY = 0;
            let isDragging = false, lastX = 0, lastY = 0;
            function applyTransform() {
                contentElem.style.transform = `scale(${scale}) translate(${panX}px, ${panY}px)`;
                contentElem.style.transformOrigin = 'center center';
            }
            btnPlus.onclick = function(e) { e.stopPropagation(); scale *= 1.2; applyTransform(); };
            btnMinus.onclick = function(e) { e.stopPropagation(); scale /= 1.2; applyTransform(); };
            btnReset.onclick = function(e) { e.stopPropagation(); scale = 1; panX = 0; panY = 0; applyTransform(); };
            // 拖拽平移（事件全部绑定在overlay内部，避免外部影响）
            contentElem.addEventListener('mousedown', function(e) {
                isDragging = true;
                lastX = e.clientX;
                lastY = e.clientY;
                contentElem.style.cursor = 'grab';
                e.stopPropagation();
                e.preventDefault();
            });
            overlay.addEventListener('mousemove', function(e) {
                if (isDragging) {
                    panX += (e.clientX - lastX);
                    panY += (e.clientY - lastY);
                    lastX = e.clientX;
                    lastY = e.clientY;
                    applyTransform();
                }
            });
            // 只允许点击overlay空白区域且非拖拽时关闭
            overlay.addEventListener('mousedown', function(e) {
                overlay._maybeClose = (e.target === overlay);
            });
            // mouseup全局监听，setTimeout确保isDragging已重置
            document.addEventListener('mouseup', function(e) {
                if (isDragging) {
                    isDragging = false;
                    contentElem.style.cursor = 'zoom-in';
                }
                setTimeout(function() {
                    if (!isDragging && overlay._maybeClose && e.target === overlay) {
                        document.body.removeChild(overlay);
                    }
                }, 0);
            });
            // 内容
            contentElem.style.boxShadow = '0 4px 32px rgba(0,0,0,0.3)';
            contentElem.style.borderRadius = '8px';
            contentElem.style.background = '#fff';
            contentElem.style.transition = 'transform 0.2s';
            applyTransform();
            container.appendChild(controls);
            container.appendChild(contentElem);
            overlay.appendChild(container);
            return overlay;
        }
        document.body.addEventListener('click', function(e) {
            // 图片放大
            let img = e.target.closest('.markdown-body img');
            if (img) {
                if (img.classList.contains('zoomed')) return;
                let bigImg = document.createElement('img');
                bigImg.src = img.src;
                bigImg.className = img.className + ' zoomed';
                let overlay = createZoomOverlay(bigImg);
                document.body.appendChild(overlay);
                return;
            }
            // Mermaid图放大
            let mermaidDiv = e.target.closest('.markdown-body .mermaid');
            if (mermaidDiv) {
                if (mermaidDiv.classList.contains('zoomed')) return;
                let bigDiv = document.createElement('div');
                bigDiv.innerHTML = mermaidDiv.innerHTML;
                bigDiv.className = mermaidDiv.className + ' zoomed';
                let overlay = createZoomOverlay(bigDiv);
                document.body.appendChild(overlay);
            }
        }, false);
    });
    </script>
    '''
    return html_body + zoom_js_css 