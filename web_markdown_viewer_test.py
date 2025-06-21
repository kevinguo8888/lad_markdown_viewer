from flask import Flask, request, Response
import os

# ----------------- 重构部分开始 -----------------
# 从新的包名 lad_markdown_viewer 中导入渲染函数
from lad_markdown_viewer.markdown_processor import render_markdown_to_html
# ----------------- 重构部分结束 -----------------

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    md_path = request.args.get('md', 'D:/lad/LAD_Project/07_Templates_Standards/04_Naming_Conventions/LAD-07-04-001.md')
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
    except Exception as e:
        md_text = f"无法读取文件: {e}"

    # ----------------- 重构部分 -----------------
    # 只需一行代码即可完成所有Markdown处理
    html_body = render_markdown_to_html(md_text)
    # ----------------- 重构结束 -----------------

    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <script src="https://cdn.jsdelivr.net/npm/mermaid@9.4.3/dist/mermaid.min.js"></script>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                try {
                    if (typeof mermaid !== 'undefined') {
                        mermaid.initialize({
                            startOnLoad: true,
                            theme: 'default',
                            securityLevel: 'loose',
                            flowchart: { htmlLabels: true, useMaxWidth: true },
                        });
                    }
                } catch(e) {
                    console.error('Mermaid initialization error:', e);
                }
            });
        </script>
        <style>
            body { font-family: '微软雅黑', Arial, sans-serif; margin: 30px; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
            th { background: #f6f8fa; }
            pre { background: #f6f8fa; padding: 10px; border-radius: 4px; }
            code { background: #f6f8fa; padding: 2px 4px; border-radius: 4px; }
            .mermaid { background: white; padding: 10px; border-radius: 4px; text-align: center; }
        </style>
    </head>
    <body>
    """ + html_body + """
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True) 