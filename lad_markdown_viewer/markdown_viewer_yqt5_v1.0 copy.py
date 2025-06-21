import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import mistune
import re
import html as html_module

class MarkdownViewer(QMainWindow):
    def __init__(self, md_path):
        super().__init__()
        self.setWindowTitle("Markdown 预览")
        self.resize(900, 700)

        # 读取 markdown 文件
        with open(md_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        # 1. 提取 mermaid 代码块并用占位符替换
        def extract_mermaid_blocks(md_text):
            mermaid_blocks = []
            def replacer(match):
                mermaid_blocks.append(match.group(1).strip())
                return f"@@MERMAID{len(mermaid_blocks)-1}@@"
            new_md = re.sub(r'```mermaid\s*([\s\S]*?)\s*```', replacer, md_text)
            return new_md, mermaid_blocks

        # 2. 渲染后再还原 mermaid 代码块
        def restore_mermaid_blocks(html, mermaid_blocks):
            for i, code in enumerate(mermaid_blocks):
                html = html.replace(f"@@MERMAID{i}@@", f'<div class="mermaid">{code}</div>')
            return html

        md_text, mermaid_blocks = extract_mermaid_blocks(md_text)

        # 用 mistune 解析 markdown
        md = mistune.create_markdown(plugins=['strikethrough', 'table', 'task_lists'])
        html_body = md(md_text)
        html_body = html_module.unescape(html_body)
        html_body = restore_mermaid_blocks(html_body, mermaid_blocks)

        # 兜底修正：解包被<pre><code>包裹的表格和列表
        def fix_pre_code_blocks(html):
            pattern = re.compile(r'<pre><code>(.*?(<table|<ul|<ol|<thead|<tbody|<tr|<li).*?)</code></pre>', re.DOTALL)
            def repl(m):
                return m.group(1)
            return pattern.sub(repl, html)
        html_body = fix_pre_code_blocks(html_body)

        # 包裹为完整 HTML 文档
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

        # 输出完整HTML代码，便于核查
        print("\n===== 解析后完整HTML代码 =====\n")
        print(html)
        print("\n===== END =====\n")

        # 设置 QWebEngineView
        self.browser = QWebEngineView()
        self.browser.setHtml(html)

        # 布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.browser)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = MarkdownViewer('D:/lad/LAD_Project/00_Platform_Strategy/02_Strategic_Subdocs/01_Platform_Model/LAD-00-02-01-001.md')
    viewer.show()
    sys.exit(app.exec_())
