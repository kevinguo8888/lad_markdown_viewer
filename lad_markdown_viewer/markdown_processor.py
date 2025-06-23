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