import re

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