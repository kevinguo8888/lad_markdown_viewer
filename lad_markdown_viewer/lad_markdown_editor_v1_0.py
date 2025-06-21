# -*- coding: utf-8 -*-
"""
LAD Markdown 可视编辑器 (Tkinter GUI 工具)
版本：v1.0
依赖：tkinter, tkhtmlview
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkhtmlview import HTMLLabel
import os
import re
import datetime
import shutil

# 预设 LAD 段落模板
default_templates = {
    "平台概述": "## 平台概述\nLAD平台致力于打造透明、公正的贷款撮合机制。",
    "合作机制": "## 合作机制\n平台支持多类型主体合作，规则公开透明。"
}

class MarkdownEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LAD Markdown 可视编辑器")
        self.root.geometry("1000x600")
        self.force_timestamp = tk.BooleanVar(value=True)

        self.current_file = None
        self.paragraphs = []
        self.original_content = ""

        self.create_widgets()

    def create_widgets(self):
        # 顶部按钮栏
        toolbar = tk.Frame(self.root)
        toolbar.pack(side="top", fill="x")

        tk.Button(toolbar, text="打开文件", command=self.load_file).pack(side="left")
        tk.Button(toolbar, text="保存修改", command=self.save_changes).pack(side="left")
        tk.Button(toolbar, text="追加段落", command=self.insert_template).pack(side="left")
        tk.Checkbutton(toolbar, text="强制追加时间戳", variable=self.force_timestamp).pack(side="left")

        # 中间区域布局
        content_frame = tk.Frame(self.root)
        content_frame.pack(expand=True, fill="both")

        # 左侧：段落列表 + 渲染预览
        left_frame = tk.Frame(content_frame, width=300)
        left_frame.pack(side="left", fill="y")
        tk.Label(left_frame, text="段落选择").pack()
        self.paragraph_selector = tk.Listbox(left_frame)
        self.paragraph_selector.pack(fill="y", expand=True)
        self.paragraph_selector.bind("<<ListboxSelect>>", self.display_paragraph)
        self.preview = HTMLLabel(left_frame, html="")
        self.preview.pack(fill="both", expand=True)

        # 右侧：编辑区
        right_frame = tk.Frame(content_frame)
        right_frame.pack(side="right", fill="both", expand=True)
        tk.Label(right_frame, text="段落内容").pack()
        self.editor = tk.Text(right_frame, wrap="word")
        self.editor.pack(fill="both", expand=True)

    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
        if not path:
            return
        self.current_file = path
        with open(path, "r", encoding="utf-8") as f:
            self.original_content = f.read()
        self.extract_paragraphs()
        messagebox.showinfo("提示", f"成功加载文件：{os.path.basename(path)}")

    def extract_paragraphs(self):
        self.paragraphs.clear()
        self.paragraph_selector.delete(0, tk.END)
        pattern = r"(?m)^(#{1,3})\s*(.+?)\s*$"
        self.paragraph_map = {}
        for match in re.finditer(pattern, self.original_content):
            header = match.group(0)
            title = match.group(2)
            self.paragraphs.append((title, match.start(), match.end()))
            self.paragraph_selector.insert(tk.END, title)
            self.paragraph_map[title] = match.start()

    def display_paragraph(self, event):
        selection = self.paragraph_selector.get(tk.ACTIVE)
        start = self.paragraph_map.get(selection)
        if start is None:
            return

        next_titles = [p[1] for p in self.paragraphs if p[1] > start]
        end = min(next_titles) if next_titles else len(self.original_content)

        segment = self.original_content[start:end].strip()
        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", segment)
        self.preview.set_html(self.md_to_html(segment))

    def md_to_html(self, text):
        html = text.replace("\n", "<br>")
        html = re.sub(r"^### (.*?)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
        html = re.sub(r"^## (.*?)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
        html = re.sub(r"^# (.*?)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)
        return html

    def save_changes(self):
        if not self.current_file:
            return
        selected = self.paragraph_selector.get(tk.ACTIVE)
        if selected not in self.paragraph_map:
            return

        # 备份原文件
        bak_file = self.current_file.replace(".md", ".bak.md")
        shutil.copyfile(self.current_file, bak_file)

        # 获取修改内容
        edited = self.editor.get("1.0", tk.END).strip()
        if self.force_timestamp.get():
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            edited += f"\n\n<!-- 编辑时间：{timestamp} -->"

        lines = self.original_content.splitlines()
        pattern = re.compile(rf"(?m)^#+\s*{re.escape(selected)}\s*$")
        found = False
        for i, line in enumerate(lines):
            if pattern.match(line):
                found = True
                start = i
                break
        if not found:
            messagebox.showerror("错误", "段落起始行未找到")
            return

        # 查找段落结束
        end = len(lines)
        for j in range(start + 1, len(lines)):
            if re.match(r"^#+\s", lines[j]):
                end = j
                break

        # 替换段落内容
        edited_lines = edited.splitlines()
        lines[start:end] = edited_lines
        self.original_content = "\n".join(lines)

        # 追加至编辑日志
        self.append_edit_log(selected)

        # 保存
        with open(self.current_file, "w", encoding="utf-8") as f:
            f.write(self.original_content)

        messagebox.showinfo("成功", "修改已保存并记录日志")

    def append_edit_log(self, title):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = f"- {timestamp} 修改段落：{title}"
        if "## 编辑日志" not in self.original_content:
            self.original_content += "\n\n## 编辑日志\n"
        self.original_content += f"\n{log}"

    def insert_template(self):
        template_name = tk.simpledialog.askstring("模板名", "请输入段落模板名：平台概述/合作机制")
        if not template_name:
            return
        if template_name not in default_templates:
            messagebox.showerror("错误", "模板不存在")
            return
        content = default_templates[template_name]
        if self.force_timestamp.get():
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            content += f"\n\n<!-- 编辑时间：{timestamp} -->"
        self.original_content += f"\n\n{content}"
        with open(self.current_file, "w", encoding="utf-8") as f:
            f.write(self.original_content)
        messagebox.showinfo("成功", f"已追加模板段落：{template_name}")
        self.extract_paragraphs()

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownEditorApp(root)
    root.mainloop()
