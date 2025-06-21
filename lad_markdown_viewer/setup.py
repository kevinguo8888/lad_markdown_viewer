#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LAD Markdown Viewer Setup

一个功能强大的Markdown查看器，支持Web和桌面应用。

许可证: MIT License
适用范围: 核心Markdown处理功能、Web应用
注意: 桌面应用模块使用GPL v3许可证（由于PyQt5依赖）

作者: LAD Markdown Viewer Contributors
版本: 1.2.0
"""

from setuptools import setup, find_packages
import os

# 读取README文件
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "A powerful Markdown viewer with YAML front-matter and Mermaid support"

# 读取requirements文件
def read_requirements(filename):
    requirements_path = os.path.join(os.path.dirname(__file__), '..', filename)
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="lad-markdown-viewer",
    version="1.2.0",
    author="LAD Markdown Viewer Contributors",
    author_email="kositguo@gmail.com",
    description="一个功能强大的Markdown查看器，支持Web和桌面应用",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/lad-markdown-viewer/lad-markdown-viewer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Text Processing :: Markup",
        "Topic :: Software Development :: Documentation",
        "Topic :: Desktop Environment",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements('requirements-core.txt'),
    extras_require={
        'desktop': read_requirements('requirements-desktop.txt'),
        'web': [
            'flask>=2.0.0',
            'flask-cors>=3.0.0',
        ],
        'dev': [
            'pytest>=6.0.0',
            'pytest-cov>=2.10.0',
            'pytest-html>=3.0.0',
            'black>=21.0.0',
            'flake8>=3.8.0',
            'mypy>=0.800',
        ],
    },
    entry_points={
        'console_scripts': [
            'lad-markdown-viewer=lad_markdown_viewer.ladmark_viewer:main',
            'lad-markdown-web=lad_markdown_viewer.web_viewer:main',
        ],
    },
    include_package_data=True,
    package_data={
        'lad_markdown_viewer': ['*.md', '*.txt', '*.html'],
    },
    keywords=[
        'markdown', 'viewer', 'renderer', 'html', 'desktop', 'web', 
        'gui', 'qt', 'flask', 'mermaid', 'yaml', 'toc'
    ],
    project_urls={
        'Homepage': 'https://github.com/lad-markdown-viewer/lad-markdown-viewer',
        'Documentation': 'https://github.com/lad-markdown-viewer/lad-markdown-viewer/blob/main/README.md',
        'Repository': 'https://github.com/lad-markdown-viewer/lad-markdown-viewer',
        'Bug Tracker': 'https://github.com/lad-markdown-viewer/lad-markdown-viewer/issues',
        'Changelog': 'https://github.com/lad-markdown-viewer/lad-markdown-viewer/blob/main/CHANGELOG.md',
    },
) 