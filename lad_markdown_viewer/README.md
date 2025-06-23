# LAD Markdown Viewer

一个功能强大的Markdown查看器，支持Web和桌面应用，具有完整的Markdown渲染、目录导航、YAML前置元数据解析等功能。

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

## 功能特性

### 核心功能
- **完整的Markdown渲染**：支持标准Markdown语法
- **YAML前置元数据解析**：自动解析文档头部的YAML元数据并显示为表格
- **Mermaid图表支持**：渲染流程图、时序图等Mermaid图表
- **可点击目录导航**：自动生成目录，支持锚点跳转
- **代码高亮**：支持多种编程语言的语法高亮

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

## 安装

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

## 使用方法

### Web应用
```bash
python web_markdown_viewer_test.py
```
访问 `http://localhost:5000` 查看Web界面

### 桌面应用
```bash
python markdown_viewer_yqt5.py
```

### 作为包使用
```python
from lad_markdown_viewer.markdown_processor import MarkdownProcessor

processor = MarkdownProcessor()
html_content = processor.process_markdown(markdown_content)
```

## 项目结构

```
lad_markdown_viewer/
├── __init__.py                 # 包初始化文件
├── markdown_processor.py       # 核心Markdown处理逻辑
├── markdown_utils.py          # 工具函数
├── ladmark_viewer.py          # PyQt5桌面应用 (GPL v3)
├── markdown_viewer_component.py # 组件化视图
├── markdown_editor.py         # 编辑器组件
├── gui_markdown.py           # GUI相关功能
├── Console_Mark.py           # 控制台版本
├── lad_markdown_editor_v1_0.py # 编辑器v1.0
├── lad_markdown_editor_v1_1.py # 编辑器v1.1
├── example.md                # 示例文档
├── output.html               # 输出示例
├── README.md                 # 项目说明
├── CHANGELOG.md              # 变更日志
├── LICENSE                   # 许可证
├── CONTRIBUTING.md           # 贡献指南
├── API.md                    # API文档
├── EXAMPLES.md               # 使用示例
├── TESTING.md                # 测试说明
└── setup.py                  # 安装配置
```

## 配置选项

### Markdown处理器配置
- 支持自定义CSS样式
- 可配置Mermaid主题
- 可调整代码高亮主题

### 应用配置
- Web服务器端口配置
- 桌面应用窗口大小
- 文件编码设置

## 开发

### 代码规范
- 遵循PEP 8编码规范
- 使用类型注解
- 添加适当的文档字符串

### 测试
```bash
# 运行测试
python -m pytest tests/
```

## 许可证

- **核心库**: MIT 许可证 - 详见 [LICENSE](LICENSE) 文件
- **桌面应用**: GPL v3 许可证 - 由于PyQt5依赖要求

## 贡献

欢迎提交Issue和Pull Request！详见 [CONTRIBUTING.md](CONTRIBUTING.md)

## 更新日志

详见 [CHANGELOG.md](CHANGELOG.md)

---

**最后更新**：2025-06-23 10:42
**版本**：v1.3.0
