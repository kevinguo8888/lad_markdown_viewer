from flask import Flask, request, Response
import os

# ----------------- 重构部分开始 -----------------
# 从新的包名 lad_markdown_viewer 中导入渲染函数
# from lad_markdown_viewer.markdown_processor import render_markdown_to_html
from lad_markdown_viewer.markdown_processor import render_markdown_with_zoom
# ----------------- 重构部分结束 -----------------

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    md_path = request.args.get('md', 'D:/lad/LAD_Project/00_Platform_Strategy/02_Strategic_Subdocs/01_Platform_Model/LAD-00-02-01-001.md')

    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
    except Exception as e:
        md_text = f"无法读取文件: {e}"

    # ----------------- 重构部分 -----------------
    # 只需一行代码即可完成所有Markdown处理
    # html_body = render_markdown_to_html(md_text)
    html_body = render_markdown_with_zoom(md_text)
    # ----------------- 重构结束 -----------------

    html = """
    <html>
    <head>
        <meta charset=\"utf-8\">
        <link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/github-markdown-css@5.5.1/github-markdown.min.css\">
        <script src=\"https://cdn.jsdelivr.net/npm/mermaid@9.4.3/dist/mermaid.min.js\"></script>
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
                // 只保留a标签拦截
                document.body.addEventListener('click', function(e) {
                    let a = e.target.closest('a');
                    if (a && a.getAttribute('href')) {
                        let href = a.getAttribute('href');
                        if (href.endsWith('.md')) {
                            e.preventDefault();
                            window.location.href = '/?md=' + encodeURIComponent(href);
                        } else if (href.startsWith('http') || href.startsWith('https') || href.startsWith('ftp')) {
                            e.preventDefault();
                            if (window.onMarkdownLinkClick) {
                                window.onMarkdownLinkClick(href);
                            } else {
                                window.open(href, '_blank');
                            }
                        }
                        return;
                    }
                }, false);
            });
        </script>
        <style>
            body { font-family: '微软雅黑', Arial, sans-serif; margin: 0; background: #f6f8fa; }
            /* GitHub风格容器，内容左对齐，最大宽度居中 */
            .markdown-body {
                box-sizing: border-box;
                min-width: 200px;
                max-width: 980px;
                margin: 32px auto;
                padding: 32px;
                background: #fff;
                border-radius: 8px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            }
            .mermaid { background: white; padding: 10px; border-radius: 4px; text-align: center; }
            .markdown-body img { cursor: zoom-in; }
        </style>
    </head>
    <body>
<div class=\"markdown-body\">""" + html_body + """</div>
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True) 