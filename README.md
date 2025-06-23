# LAD Markdown Viewer 项目

[⏰ 时间：2025-06-23 10:42]

一个功能强大的Markdown查看器项目，支持Web和桌面应用，具有完整的Markdown渲染、目录导航、YAML前置元数据解析等功能。

## 许可证说明

本项目采用双许可证模式：

- **核心库** (MIT许可证): 包括Markdown处理、Web应用等核心功能
- **桌面应用** (GPL v3许可证): 由于使用PyQt5，桌面应用模块采用GPL v3许可证

### 安装选项

```bash
# 仅安装核心功能 (MIT许可证)
pip install -r requirements-core.txt

# 安装完整版本 (包含GPL v3桌面应用)
pip install -r requirements-desktop.txt
```

## 项目概述

LAD Markdown Viewer是一个基于Python的独立Markdown查看器工具，提供了以下核心功能：

- **完整的Markdown渲染**：支持标准Markdown语法
- **YAML前置元数据解析**：自动解析文档头部的YAML元数据并显示为表格
- **Mermaid图表支持**：渲染流程图、时序图等Mermaid图表
- **可点击目录导航**：自动生成目录，支持锚点跳转
- **代码高亮**：支持多种编程语言的语法高亮
- **多界面支持**：Web界面（Flask）和桌面应用（PyQt5）

## 项目结构

```
LAD_md_ed/
├── lad_markdown_viewer/          # 核心Python包
│   ├── __init__.py
│   ├── markdown_processor.py     # 核心Markdown处理逻辑
│   ├── markdown_utils.py         # 工具函数
│   ├── ladmark_viewer.py         # PyQt5桌面应用 (GPL v3)
│   ├── markdown_viewer_component.py # 组件化视图
│   ├── markdown_editor.py        # 编辑器组件
│   ├── gui_markdown.py          # GUI相关功能
│   ├── Console_Mark.py          # 控制台版本
│   ├── lad_markdown_editor_v1_0.py # 编辑器v1.0
│   ├── lad_markdown_editor_v1_1.py # 编辑器v1.1
│   ├── example.md               # 示例文档
│   ├── output.html              # 输出示例
│   ├── README.md                # 包说明文档
│   ├── CHANGELOG.md             # 变更日志
│   ├── LICENSE                  # 许可证
│   ├── CONTRIBUTING.md          # 贡献指南
│   ├── API.md                   # API文档
│   ├── EXAMPLES.md              # 使用示例
│   ├── TESTING.md               # 测试说明
│   └── setup.py                 # 安装配置
├── web_markdown_viewer_test.py  # Flask Web应用入口
├── markdown_viewer_yqt5.py      # PyQt5桌面应用入口
├── requirements.txt             # 项目依赖
├── requirements-core.txt        # 核心依赖 (MIT兼容)
├── requirements-desktop.txt     # 桌面依赖 (GPL v3)
├── README.markdown_viewer.md    # 项目说明
├── 版权和许可证分析报告.md       # 许可证分析
└── docs/                        # 项目文档
    └── 需求与技术方案.md
```

## 快速开始

### 环境要求

- Python 3.7+
- 依赖包：见 `requirements-core.txt` 或 `requirements-desktop.txt`

### 安装步骤

```bash
# 克隆项目
git clone <repository-url>
cd LAD_md_ed

# 安装依赖（选择其一）
pip install -r requirements-core.txt      # 仅核心功能
pip install -r requirements-desktop.txt   # 包含桌面应用
```

### 使用方法

#### Web应用
```bash
python web_markdown_viewer_test.py
```
访问 `http://localhost:5000` 查看Web界面

#### 桌面应用
```bash
python markdown_viewer_yqt5.py
```

#### 作为包使用
```python
from lad_markdown_viewer.markdown_processor import MarkdownProcessor

processor = MarkdownProcessor()
html_content = processor.process_markdown(markdown_content)
```

## 功能特性

### 核心功能
- **Markdown转HTML**：使用 `mistune` 作为核心转换引擎
- **YAML Front-Matter**：自动解析文档头部的YAML元信息，并将其渲染为一个美观的HTML表格
- **目录跳转 (TOC)**：自动为各级标题生成锚点ID，支持目录链接的精准跳转
- **Mermaid图表**：支持在Markdown中嵌入 `mermaid` 语法，并正确渲染出图表
- **GUI组件**：内置一个基于 `PyQt5` 的 `LadMark` 控件，可以方便地集成到任何桌面应用程序中

### 插件支持
- 表格渲染 (`table`)
- 任务列表 (`task_lists`)
- 删除线 (`strikethrough`)
- 自动链接 (`url`)
- 脚注 (`footnotes`)

### 应用界面
- **Web界面**：基于Flask的Web应用
- **桌面应用**：基于PyQt5的桌面应用
- **响应式设计**：适配不同屏幕尺寸

## 开发指南

### 代码规范
- 遵循PEP 8编码规范
- 使用类型注解
- 添加适当的文档字符串

### 测试
```bash
# 运行测试
python -m pytest tests/
```

### 贡献
欢迎提交Issue和Pull Request！详见 [CONTRIBUTING.md](lad_markdown_viewer/CONTRIBUTING.md)

## 文档

- [API文档](lad_markdown_viewer/API.md) - 详细的API接口说明
- [使用示例](lad_markdown_viewer/EXAMPLES.md) - 丰富的使用案例
- [测试说明](lad_markdown_viewer/TESTING.md) - 测试策略和用例
- [变更日志](lad_markdown_viewer/CHANGELOG.md) - 版本更新历史
- [版权和许可证分析报告](版权和许可证分析报告.md) - 详细的许可证分析

## 许可证

- **核心库**: MIT 许可证 - 详见 [LICENSE](lad_markdown_viewer/LICENSE) 文件
- **桌面应用**: GPL v3 许可证 - 由于PyQt5依赖要求

## 更新日志

详见 [CHANGELOG.md](lad_markdown_viewer/CHANGELOG.md)

---

**最后更新**：2025-06-23 10:42  
**版本**：v1.3.0  
**维护者**：LAD Markdown Viewer Contributors