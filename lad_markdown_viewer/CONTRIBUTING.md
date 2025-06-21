# 贡献指南

感谢您对LAD Markdown Viewer项目的关注！我们欢迎所有形式的贡献。

## 如何贡献

### 报告Bug
1. 使用GitHub Issues报告bug
2. 提供详细的复现步骤
3. 包含错误信息和系统环境

### 功能请求
1. 在Issues中提出新功能建议
2. 详细描述功能需求和用例
3. 讨论实现方案

### 代码贡献
1. Fork项目仓库
2. 创建功能分支
3. 提交代码更改
4. 创建Pull Request

## 开发环境设置

### 环境要求
- Python 3.7+
- Git
- 推荐使用虚拟环境

### 安装步骤
```bash
# 克隆项目
git clone https://github.com/your-username/LAD_md_ed.git
cd LAD_md_ed

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

## 代码规范

### Python代码风格
- 遵循PEP 8编码规范
- 使用4个空格缩进
- 行长度不超过120字符
- 使用类型注解

### 文档规范
- 所有公共函数必须有文档字符串
- 使用Google风格的文档字符串
- 更新相关文档

### 提交信息规范
使用语义化提交信息：
- `feat:` 新功能
- `fix:` 修复bug
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具的变动

## 测试

### 运行测试
```bash
# 运行所有测试
python -m pytest

# 运行特定测试文件
python -m pytest tests/test_markdown_processor.py

# 生成覆盖率报告
python -m pytest --cov=lad_markdown_viewer
```

### 测试要求
- 新功能必须包含测试
- 修复bug必须包含回归测试
- 测试覆盖率不低于80%

## Pull Request流程

### 提交前检查
1. 代码通过所有测试
2. 符合代码规范
3. 更新相关文档
4. 更新CHANGELOG.md

### PR描述
- 清晰描述更改内容
- 关联相关Issue
- 提供测试结果
- 包含截图（如适用）

## 发布流程

### 版本发布
1. 更新版本号
2. 更新CHANGELOG.md
3. 创建Git标签
4. 发布到PyPI（如适用）

## 行为准则

### 社区准则
- 尊重所有贡献者
- 保持专业和友善
- 欢迎新手贡献者
- 提供建设性反馈

### 沟通渠道
- GitHub Issues
- GitHub Discussions
- 邮件列表（如适用）

## 许可证

贡献的代码将采用与项目相同的MIT许可证。

---

**最后更新**：2025-06-21 19:47 