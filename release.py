#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LAD Markdown Viewer 发布脚本
自动化版本发布流程

[⏰ 时间：2025-06-23 10:42]
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, cwd=None):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ 命令执行失败: {cmd}")
            print(f"错误信息: {result.stderr}")
            return False, result.stderr
        return True, result.stdout
    except Exception as e:
        print(f"❌ 命令执行异常: {cmd}")
        print(f"异常信息: {e}")
        return False, str(e)

def check_environment():
    """检查发布环境"""
    print("🔍 检查发布环境...")
    
    # 检查必要的工具
    tools = ['python', 'pip', 'git']
    for tool in tools:
        success, _ = run_command(f'where {tool}' if os.name == 'nt' else f'which {tool}')
        if not success:
            print(f"❌ 缺少必要工具: {tool}")
            return False
        print(f"✅ {tool} 已安装")
    
    # 检查Git状态
    success, output = run_command('git status --porcelain')
    if success and output.strip():
        print("⚠️  工作目录有未提交的更改")
        print("建议先提交所有更改后再发布")
        return False
    
    print("✅ 环境检查通过")
    return True

def run_tests():
    """运行测试"""
    print("🧪 运行测试...")
    
    # 检查导入
    try:
        from lad_markdown_viewer.markdown_processor import render_markdown_to_html
        print("✅ 包导入测试通过")
    except ImportError as e:
        print(f"❌ 包导入失败: {e}")
        return False
    
    # 基本功能测试
    try:
        test_md = "# 测试\n\n- [x] 任务\n\n| 列1 | 列2 |\n|-----|-----|\n| 数据1 | 数据2 |"
        html = render_markdown_to_html(test_md)
        if '<table>' in html and 'type="checkbox"' in html:
            print("✅ 基本功能测试通过")
        else:
            print("❌ 基本功能测试失败")
            return False
    except Exception as e:
        print(f"❌ 功能测试异常: {e}")
        return False
    
    return True

def build_package():
    """构建包"""
    print("📦 构建包...")
    
    # 清理旧的构建文件
    dirs_to_clean = ['build', 'dist', 'lad_markdown_viewer.egg-info']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"🧹 清理 {dir_name}")
    
    # 构建源码包和wheel包
    success, output = run_command('python lad_markdown_viewer/setup.py sdist bdist_wheel')
    if not success:
        print("❌ 包构建失败")
        return False
    
    print("✅ 包构建完成")
    return True

def check_package():
    """检查包的完整性"""
    print("🔍 检查包完整性...")
    
    # 检查构建文件是否存在
    if not os.path.exists('dist'):
        print("❌ dist目录不存在")
        return False
    
    dist_files = os.listdir('dist')
    if not dist_files:
        print("❌ dist目录为空")
        return False
    
    print(f"✅ 找到构建文件: {', '.join(dist_files)}")
    
    # 尝试安装测试
    print("🧪 测试安装...")
    # 找到wheel文件
    wheel_files = [f for f in dist_files if f.endswith('.whl')]
    if wheel_files:
        wheel_path = os.path.join('dist', wheel_files[0])
        success, _ = run_command(f'pip install --dry-run "{wheel_path}"')
        if not success:
            print("❌ 包安装测试失败")
            return False
    else:
        print("❌ 未找到wheel文件")
        return False
    
    print("✅ 包检查通过")
    return True

def create_git_tag():
    """创建Git标签"""
    print("🏷️  创建Git标签...")
    
    # 读取版本号
    try:
        from lad_markdown_viewer import __version__
        version = __version__
    except ImportError:
        print("❌ 无法读取版本号")
        return False
    
    tag_name = f"v{version}"
    
    # 检查标签是否已存在
    success, _ = run_command(f'git tag -l {tag_name}')
    if success:
        print(f"⚠️  标签 {tag_name} 已存在")
        return True
    
    # 创建标签
    success, _ = run_command(f'git tag -a {tag_name} -m "Release {tag_name}"')
    if not success:
        print(f"❌ 创建标签失败: {tag_name}")
        return False
    
    print(f"✅ 创建标签: {tag_name}")
    return True

def generate_release_notes():
    """生成发布说明"""
    print("📝 生成发布说明...")
    
    try:
        from lad_markdown_viewer import __version__
        version = __version__
    except ImportError:
        print("❌ 无法读取版本号")
        return False
    
    release_notes = f"""# LAD Markdown Viewer v{version} 发布说明

## 🎉 版本亮点

### 重大重构 - 代码精简25%
- 重构 `preview_md.py` 使用统一的包架构
- 消除重复代码，从224行减少到168行
- 统一使用 `lad_markdown_viewer.markdown_processor.render_markdown_to_html`

### 🔧 功能改进
- ✅ 优化预览工具的用户体验和帮助信息
- ✅ 修复Windows控制台编码问题
- ✅ 增强错误处理和用户提示
- ✅ 统一所有应用的Markdown处理逻辑

### 🏗️ 架构优化
- 完全消除代码重复，提高维护性
- 统一的功能特性支持（YAML表格、TOC跳转、Mermaid等）
- 更好的模块化设计

## 📦 安装方式

```bash
pip install lad-markdown-viewer=={version}
```

## 🚀 快速开始

### Web应用
```bash
python web_markdown_viewer_test.py
```

### 桌面应用
```bash
python markdown_viewer_yqt5.py
```

### 预览工具
```bash
python preview_md.py your_file.md
```

## 📈 性能提升
- 代码行数减少25%
- 更快的启动时间
- 更少的内存占用
- 统一的处理逻辑

---

**发布时间**: 2025-06-23 10:42
**版本**: v{version}
**维护者**: LAD Markdown Viewer Contributors
"""
    
    with open('RELEASE_NOTES.md', 'w', encoding='utf-8') as f:
        f.write(release_notes)
    
    print("✅ 发布说明已生成: RELEASE_NOTES.md")
    return True

def main():
    """主发布流程"""
    print("🚀 LAD Markdown Viewer 发布流程")
    print("=" * 50)
    
    # 发布步骤
    steps = [
        ("环境检查", check_environment),
        ("运行测试", run_tests),
        ("构建包", build_package),
        ("检查包", check_package),
        ("创建标签", create_git_tag),
        ("生成发布说明", generate_release_notes),
    ]
    
    for step_name, step_func in steps:
        print(f"\n📋 执行步骤: {step_name}")
        print("-" * 30)
        
        if not step_func():
            print(f"❌ {step_name}失败，发布中止")
            return False
        
        print(f"✅ {step_name}完成")
    
    print("\n🎉 发布流程完成！")
    print("=" * 50)
    
    try:
        from lad_markdown_viewer import __version__
        version = __version__
    except ImportError:
        version = "unknown"
    
    print(f"📦 版本: v{version}")
    print(f"📁 构建文件: dist/")
    print(f"📝 发布说明: RELEASE_NOTES.md")
    print(f"🏷️  Git标签: v{version}")
    
    print("\n📋 后续步骤:")
    print("1. 检查构建文件")
    print("2. 推送到远程仓库: git push origin main --tags")
    print("3. 上传到PyPI: twine upload dist/*")
    print("4. 创建GitHub Release")
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1) 