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

## 组件简介

`lad_markdown_viewer` 是一款支持 Markdown 图片和 Mermaid 流程图放大、缩小、拖拽、重置等交互的高兼容性渲染组件，适用于 Flask/Web/Python 等多种环境，具备 GitHub 风格的美观排版和健壮的事件/样式隔离能力。

## 主要特性
- Markdown 图片、Mermaid 流程图一键放大、缩小、拖拽、重置
- 放大层全局唯一，支持多图/多图表独立操作
- 事件与样式作用域隔离，外部容器和全局 CSS/JS 不影响交互
- GitHub 风格渲染，兼容表格、代码块、流程图等
- a 标签拦截与外部链接回调，支持 md 文件内部跳转和外部链接自定义处理
- 易于集成，支持 Flask/Web/Python 环境

## 安装与依赖
- Python >= 3.7
- 依赖：mistune、mermaid.js（前端CDN）、github-markdown-css（前端CDN）
- 安装：
```bash
pip install mistune
# 前端页面需引入 mermaid.js 和 github-markdown-css
```

## 快速使用
```python
from lad_markdown_viewer.markdown_processor import render_markdown_with_zoom
html_body = render_markdown_with_zoom(md_text)
# 将 html_body 嵌入你的页面模板即可
```

## API说明
- `render_markdown_with_zoom(md_text: str) -> str`
  - 输入：Markdown 文本
  - 输出：带放大缩放交互的 HTML 片段

## 常见问题
- Q: 为什么放大层不会被外部样式影响？
  A: 组件内部采用独立 class 命名和事件绑定，最大限度隔离外部影响。
- Q: 如何自定义放大层样式？
  A: 可在前端页面自定义 .zoom-overlay、.zoom-controls 等 class。
- Q: 支持哪些浏览器？
  A: 兼容所有现代主流浏览器（Chrome/Edge/Firefox/Safari/Opera等）。

## 兼容性说明
- 推荐使用现代浏览器或基于 Chromium 的桌面/移动 WebView。
- 未来版本将支持 Shadow DOM 隔离、多端适配（详见 UPGRADE_PLAN.md）。

## 未来升级计划
- Shadow DOM 版组件，进一步提升隔离性
- 桌面端/移动端适配与兼容性检测
- iframe 沙箱与 CSP 安全增强
- 详见 UPGRADE_PLAN.md

## 版权与第三方依赖
- 本组件基于 MIT 协议开源
- 依赖 mermaid.js、github-markdown-css 等第三方库，详见 LICENSE/NOTICE
