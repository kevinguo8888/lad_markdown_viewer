# lad_markdown_editor_v1_1.py
# LAD Markdown 可视编辑器 v1.1
# 更新说明：
# ✅ 支持多文件切换
# ✅ 支持 LAD 模板段落下拉选择追加
# ✅ 段落提取机制优化
# ✅ 支持“撤销上次修改”

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkhtmlview import HTMLLabel
from datetime import datetime
import re
import shutil

history_stack = []  # 用于撤销操作的历史记录

class MarkdownEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("LAD Markdown 可视编辑器 v1.1")
        self.filename = None
        self.templates_dir = "templates"

        # 文件选择区
        self.file_dropdown = ttk.Combobox(root, postcommand=self.update_file_list)
        self.file_dropdown.bind("<<ComboboxSelected>>", self.load_selected_file)
        self.file_dropdown.pack(fill='x')

        # 段落选择区
        self.section_selector = ttk.Combobox(root, postcommand=self.update_section_list)
        self.section_selector.bind("<<ComboboxSelected>>", self.display_section)
        self.section_selector.pack(fill='x')

        # 渲染预览区
        self.preview_frame = HTMLLabel(root, html="<h3>预览内容</h3>")
        self.preview_frame.pack(side='left', fill='both', expand=True)

        # 编辑区
        self.editor = tk.Text(root, wrap='word', height=20, width=60)
        self.editor.pack(side='right', fill='both', expand=True)

        # 控制按钮
        button_frame = tk.Frame(root)
        button_frame.pack(fill='x')
        tk.Button(button_frame, text="保存修改", command=self.save_changes).pack(side='left')
        tk.Button(button_frame, text="撤销修改", command=self.undo_last_change).pack(side='left')
        tk.Button(button_frame, text="插入锚点", command=self.insert_anchor).pack(side='left')

        # 模板段插入
        self.template_dropdown = ttk.Combobox(button_frame, values=self.load_template_names())
        self.template_dropdown.pack(side='left')
        tk.Button(button_frame, text="追加模板段落", command=self.insert_template_section).pack(side='left')

        # 时间戳控制
        self.force_timestamp = tk.BooleanVar(value=True)
        tk.Checkbutton(button_frame, text="强制追加时间戳", variable=self.force_timestamp).pack(side='right')

    def update_file_list(self):
        md_files = [f for f in os.listdir('.') if f.endswith('.md') and not f.endswith('.bak.md')]
        self.file_dropdown['values'] = md_files

    def load_selected_file(self, event=None):
        self.filename = self.file_dropdown.get()
        self.load_file()

    def load_file(self):
        if not self.filename:
            return
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()
        self.update_section_list()

    def update_section_list(self):
        self.sections = []
        self.section_indices = []
        for i, line in enumerate(self.lines):
            if re.match(r'^(#{1,3})\s+[^#\s]', line):
                self.sections.append(line.strip())
                self.section_indices.append(i)
        self.section_selector['values'] = self.sections

    def display_section(self, event=None):
        idx = self.section_selector.current()
        if idx == -1:
            return
        start = self.section_indices[idx]
        end = self.section_indices[idx + 1] if idx + 1 < len(self.section_indices) else len(self.lines)
        section_text = ''.join(self.lines[start:end])
        self.current_section_range = (start, end)
        self.editor.delete('1.0', 'end')
        self.editor.insert('1.0', section_text)
        self.preview_frame.set_html(self.markdown_to_html(section_text))

    def markdown_to_html(self, text):
        html = text.replace("\n", "<br>").replace("# ", "<h1>").replace("## ", "<h2>").replace("### ", "<h3>")
        return html

    def save_changes(self):
        if not self.filename:
            return
        new_content = self.editor.get("1.0", "end").strip() + "\n"
        start, end = self.current_section_range
        history_stack.append((start, end, self.lines[start:end]))  # 保存原文用于撤销

        self.lines[start:end] = [line + "\n" for line in new_content.splitlines()]
        self.append_edit_log(self.sections[self.section_selector.current()])
        with open(self.filename + ".bak.md", 'w', encoding='utf-8') as f:
            f.writelines(self.lines)
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.writelines(self.lines)
        messagebox.showinfo("保存成功", "段落修改已保存")

    def undo_last_change(self):
        if history_stack:
            start, end, original_lines = history_stack.pop()
            self.lines[start:end] = original_lines
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.writelines(self.lines)
            messagebox.showinfo("撤销成功", "已恢复至上一次保存前状态")
        else:
            messagebox.showwarning("无操作", "无可撤销内容")

    def append_edit_log(self, section_title):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log = f"\n### [{timestamp}] 修改段落：{section_title}\n"
        for i, line in enumerate(self.lines):
            if line.strip() == '## 编辑日志':
                self.lines.insert(i + 1, log)
                break

    def insert_template_section(self):
        tpl_name = self.template_dropdown.get()
        tpl_path = os.path.join(self.templates_dir, f"{tpl_name}.md")
        if os.path.exists(tpl_path):
            with open(tpl_path, 'r', encoding='utf-8') as f:
                tpl_content = f.read()
            if self.force_timestamp.get():
                tpl_content += f"\n<!-- inserted at {datetime.now()} -->\n"
            self.lines.append('\n' + tpl_content)
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.writelines(self.lines)
            messagebox.showinfo("模板追加", f"已插入模板段落：{tpl_name}")

    def insert_anchor(self):
        anchor = f"<!-- anchor:{datetime.now().timestamp()} -->\n"
        self.editor.insert("insert", anchor)

    def load_template_names(self):
        if not os.path.exists(self.templates_dir):
            return []
        return [f[:-3] for f in os.listdir(self.templates_dir) if f.endswith(".md")]

if __name__ == '__main__':
    root = tk.Tk()
    app = MarkdownEditor(root)
    root.mainloop()
