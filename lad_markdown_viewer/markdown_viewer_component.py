import sys
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import markdown
import pymdownx.superfences
import re
import html as html_module

class MarkdownViewerWidget(QWidget):
    def __init__(self, markdown_path, parent=None):
        super().__init__(parent)
        self.markdown_path = markdown_path
        self.browser = QWebEngineView()
        self.init_ui()
        self.load_markdown()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.browser)
        self.setLayout(layout)

    def load_markdown(self):
        with open(self.markdown_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
        html_body = markdown.markdown(
            md_text,
            extensions=[
                'extra', 'codehilite', 'toc',
                'pymdownx.superfences'
            ],
            extension_configs={
                'pymdownx.superfences': {
                    'custom_fences': [
                        {
                            'name': 'mermaid',
                            'class': 'mermaid',
                            'format': pymdownx.superfences.fence_div_format
                        }
                    ]
                }
            }
        )
        # 兜底正则替换
        def codeblock_to_mermaid_div(html):
            pattern = re.compile(r'<pre><code class="language-mermaid">(.*?)</code></pre>', re.DOTALL)
            return pattern.sub(lambda m: f'<div class="mermaid">{m.group(1)}</div>', html)
        html_body = codeblock_to_mermaid_div(html_body)
        html_body = html_module.unescape(html_body)
        html = f"""
        <html>
        <head>
            <meta charset=\"utf-8\">
            <script src=\"https://unpkg.com/mermaid@8.13.10/dist/mermaid.min.js\" onload=\"mermaid.initialize({{startOnLoad:true}});\"></script>
            <style>
                body {{ font-family: '微软雅黑', Arial, sans-serif; margin: 30px; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
                th {{ background: #f6f8fa; }}
                pre {{ background: #f6f8fa; padding: 10px; border-radius: 4px; }}
                code {{ background: #f6f8fa; padding: 2px 4px; border-radius: 4px; }}
            </style>
        </head>
        <body>
        {html_body}
        </body>
        </html>
        """
        self.browser.setHtml(html) 