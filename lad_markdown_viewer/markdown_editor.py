import markdown
from pygments.formatters import HtmlFormatter

# 加载你的 markdown 文件
with open('D:\lad\LAD_Project\README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 使用 markdown 库和 codehilite 扩展（带语法高亮）
html_body = markdown.markdown(
    text,
    extensions=['extra', 'codehilite', 'toc']
)

# 提取 pygments 的 CSS 样式（语法高亮）
pygments_css = HtmlFormatter().get_style_defs('.codehilite')

# 构造完整 HTML
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Markdown Render</title>
    <link rel="stylesheet" href="github-markdown.min.css">
    <style>
        body {{
            box-sizing: border-box;
            min-width: 200px;
            max-width: 980px;
            margin: 0 auto;
            padding: 45px;
        }}
        .markdown-body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
        }}
        {pygments_css}
    </style>
</head>
<body>
<article class="markdown-body">
{html_body}
</article>
</body>
</html>
"""

# 保存 HTML 到文件
with open('D:\lad\LAD_md_ed\src\README.md.html', 'w', encoding='utf-8') as f:
    f.write(html)
