import tkinter as tk
from tkhtmlview import HTMLLabel
import markdown

# 渲染 Markdown 到 HTML 字符串
with open("D:\lad\LAD_Project\README.md", "r", encoding="utf-8") as f:
    md_html = markdown.markdown(f.read())

# 用 tkinter 显示 HTMLLabel（无需保存 html 文件）
root = tk.Tk()
root.title("Markdown Viewer")
label = HTMLLabel(root, html=md_html)
label.pack(fill="both", expand=True)
root.mainloop()
