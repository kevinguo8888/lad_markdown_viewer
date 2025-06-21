# MarkdownViewerWidget 组件说明

## 简介
`MarkdownViewerWidget` 是一个基于 PyQt5 + QWebEngineView 的 Markdown 可视化渲染组件，支持常用 Markdown 语法、表格、代码高亮、目录、Mermaid 流程图等。

---

## 支持的特性
- 标准 Markdown 语法（标题、列表、引用、图片、链接、代码块等）
- 表格（extra 扩展）
- 目录（TOC）
- 代码高亮（codehilite）
- Mermaid 流程图/时序图（pymdownx.superfences + mermaid.js 8.13.10）
- 自定义 fenced code block（pymdownx.superfences）

## 不支持的特性
- 数学公式（LaTeX/MathJax）
- PlantUML、Graphviz 等其他图形语法
- 任务列表、emoji、标签页等高级扩展（如需可扩展）
- 本地图片需保证路径可访问
- 其他依赖前端新特性的 JS 库

---

## 依赖
- PyQt5
- PyQtWebEngine
- markdown
- pymdown-extensions

安装：
```bash
pip install PyQt5 PyQtWebEngine markdown pymdown-extensions
```

---

## 用法示例

```python
from markdown_viewer_component import MarkdownViewerWidget
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MarkdownViewerWidget('README.md')  # 替换为你的md文件路径
    widget.show()
    sys.exit(app.exec_())
```

---

## 备注
如需支持更多扩展（如数学公式、emoji、任务列表等），可在组件基础上扩展 pymdown-extensions 配置和前端依赖。 