"""
LAD Markdown Viewer Desktop Application

基于PyQt5的桌面Markdown查看器应用。

许可证: GPL v3
注意: 由于使用PyQt5和PyQtWebEngine（GPL v3许可证），
      此模块必须采用GPL v3许可证以符合传染性要求。

作者: LAD Markdown Viewer Contributors
版本: 1.2.0
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import mistune
from mistune.plugins.formatting import strikethrough
from mistune.plugins.table import table
from mistune.plugins.task_lists import task_lists
import html as html_module
import re
import unicodedata

# ----------------- 重构部分开始 -----------------
# 从同在包内的核心模块导入渲染函数
from .markdown_processor import render_markdown_to_html
# ----------------- 重构部分结束 -----------------

# ----------------- 新增/修改部分开始 -----------------

def slugify(text):
    """根据文档中TOC链接的格式，为标题生成匹配的ID。"""
    parts = text.split(' ', 1)
    if len(parts) == 2:
        # 处理 "1.1 标题" 这种格式
        num_part, text_part = parts
        # 移除数字部分的所有点，例如 "1.2" -> "12"
        num_part = num_part.replace('.', '')
        return f"{num_part}-{text_part}"
    else:
        # 处理 "标题" 这种没有数字前缀的格式
        return text

class TocRenderer(mistune.HTMLRenderer):
    """自定义渲染器，为标题添加ID。"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.toc_items = []

    def heading(self, text, level):
        # 使用自定义的slugify函数生成ID
        slug = slugify(text)
        self.toc_items.append((level, slug, text))
        return f'<h{level} id="{slug}">{text}</h{level}>\n'

# ----------------- 新增/修改部分结束 -----------------

try:
    from markdown_utils import extract_mermaid_blocks, restore_mermaid_blocks
except ImportError:
    def extract_mermaid_blocks(md_text):
        return md_text, []
    
    def restore_mermaid_blocks(html, mermaid_blocks):
        return html

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

class LadMark(QMainWindow):
    def __init__(self, md_path):
        super().__init__()
        self.setWindowTitle("LadMark Markdown 预览")
        self.resize(900, 700)

        with open(md_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        # ----------------- 重构部分 -----------------
        # 只需一行代码即可完成所有Markdown处理
        html_body = render_markdown_to_html(md_text)
        # ----------------- 重构结束 -----------------

        html = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <script src="https://cdn.jsdelivr.net/npm/mermaid@9.4.3/dist/mermaid.min.js"></script>
            <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    try {{
                        if (typeof mermaid !== 'undefined') {{
                            mermaid.initialize({{
                                startOnLoad: true,
                                theme: 'default',
                                securityLevel: 'loose',
                                flowchart: {{ htmlLabels: true, useMaxWidth: true }},
                            }});
                        }}
                    }} catch(e) {{
                        console.error('Mermaid initialization error:', e);
                    }}
                }});
            </script>
            <style>
                body {{ font-family: '微软雅黑', Arial, sans-serif; margin: 30px; line-height: 1.6; }}
                table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
                th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
                th {{ background: #f6f8fa; }}
                pre {{ background: #f6f8fa; padding: 10px; border-radius: 4px; overflow-x: auto; }}
                code {{ background: #f6f8fa; padding: 2px 4px; border-radius: 4px; }}
                .mermaid {{ background: white; padding: 10px; border-radius: 4px; text-align: center; }}
            </style>
        </head>
        <body>
        {html_body}
        </body>
        </html>
        """

        self.browser = QWebEngineView()
        self.browser.setHtml(html)
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.browser)
        self.setCentralWidget(central_widget) 