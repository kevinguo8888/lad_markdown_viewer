# 支持指南

[⏰ 时间：2025-06-21 19:47]

## 获取帮助

如果您在使用LAD Markdown Viewer时遇到问题，有多种方式可以获得帮助。

## 支持渠道

### 1. 文档

首先，请查看以下文档：

- **[README.md](README.md)** - 项目概述和快速开始
- **[API文档](lad_markdown_viewer/API.md)** - 详细的API参考
- **[使用示例](lad_markdown_viewer/EXAMPLES.md)** - 丰富的使用案例
- **[测试说明](lad_markdown_viewer/TESTING.md)** - 测试和故障排除
- **[变更日志](lad_markdown_viewer/CHANGELOG.md)** - 版本更新历史

### 2. GitHub Issues

对于bug报告、功能请求或一般问题：

1. 访问 [GitHub Issues](https://github.com/lad-markdown-viewer/lad-markdown-viewer/issues)
2. 搜索是否已有类似问题
3. 如果没有找到，创建新的Issue

**创建Issue时请包含**：
- 问题描述
- 重现步骤
- 环境信息（操作系统、Python版本等）
- 错误信息（如有）
- 期望行为

### 3. 电子邮件支持

对于私密问题或商业支持：

- **一般支持**: [support@lad-markdown-viewer.org]
- **技术问题**: [tech@lad-markdown-viewer.org]
- **商业咨询**: [business@lad-markdown-viewer.org]

### 4. 社区讨论

- **GitHub Discussions**: 参与社区讨论
- **Stack Overflow**: 使用标签 `lad-markdown-viewer`

## 常见问题

### 安装问题

**Q: 安装时出现依赖冲突**
A: 尝试使用虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows
pip install -r requirements-core.txt
```

**Q: PyQt5安装失败**
A: PyQt5可能需要额外的系统依赖，请参考[PyQt5安装指南](https://pypi.org/project/PyQt5/)

### 使用问题

**Q: Markdown渲染不正确**
A: 检查Markdown语法是否正确，参考[Markdown语法指南](https://www.markdownguide.org/)

**Q: Mermaid图表不显示**
A: 确保网络连接正常，Mermaid需要从CDN加载

**Q: 桌面应用无法启动**
A: 检查是否安装了桌面依赖：
```bash
pip install -r requirements-desktop.txt
```

### 许可证问题

**Q: 商业项目可以使用吗？**
A: 核心功能使用MIT许可证，可以商业使用。桌面应用使用GPL v3，需要遵循相应要求。

## 报告Bug

### Bug报告模板

```markdown
**描述**
简要描述bug

**重现步骤**
1. 步骤1
2. 步骤2
3. 步骤3

**期望行为**
描述期望的正确行为

**实际行为**
描述实际发生的错误行为

**环境信息**
- 操作系统: [如 Windows 10, macOS 12.0, Ubuntu 20.04]
- Python版本: [如 3.8.10]
- 包版本: [如 lad-markdown-viewer 1.2.0]

**错误信息**
粘贴完整的错误信息

**附加信息**
任何其他相关信息
```

## 功能请求

### 功能请求模板

```markdown
**功能描述**
详细描述您希望添加的功能

**使用场景**
描述这个功能的使用场景和好处

**实现建议**
如果有的话，提供实现建议

**优先级**
[高/中/低] - 说明优先级的原因
```

## 贡献代码

如果您想贡献代码，请查看[贡献指南](lad_markdown_viewer/CONTRIBUTING.md)。

## 响应时间

- **紧急问题**: 24小时内
- **一般问题**: 3个工作日内
- **功能请求**: 1周内评估
- **Bug报告**: 根据严重程度，1-7天内

## 商业支持

对于企业用户，我们提供：

- 优先技术支持
- 定制开发服务
- 培训和技术咨询
- SLA保证

请联系 [business@lad-markdown-viewer.org] 了解更多信息。

---

**最后更新**：2025-06-21 19:47 