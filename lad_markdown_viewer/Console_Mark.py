from rich.console import Console
from rich.markdown import Markdown

console = Console()

with open("D:\lad\LAD_md_ed\src\example.md", "r", encoding="utf-8") as f:
    md_text = f.read()

md = Markdown(md_text)
console.print(md)
