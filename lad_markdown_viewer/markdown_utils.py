import re

def slugify(text):
    """根据文档中TOC链接的格式，为标题生成匹配的ID。"""
    parts = text.split(' ', 1)
    if len(parts) == 2:
        num_part, text_part = parts
        num_part = num_part.replace('.', '')
        return f"{num_part}-{text_part}"
    else:
        return text

def extract_mermaid_blocks(md_text):
    mermaid_blocks = []
    def replacer(match):
        mermaid_blocks.append(match.group(1).strip())
        return f"@@MERMAID{len(mermaid_blocks)-1}@@"
    new_md = re.sub(r'```mermaid\s*([\s\S]*?)\s*```', replacer, md_text)
    return new_md, mermaid_blocks

def restore_mermaid_blocks(html, mermaid_blocks):
    for i, code in enumerate(mermaid_blocks):
        html = html.replace(f"@@MERMAID{i}@@", f'<div class="mermaid">{code}</div>')
    return html 