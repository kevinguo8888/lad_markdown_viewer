"""
LAD Markdown Viewer Core Library

一个功能强大的Markdown查看器核心库，提供Markdown渲染、YAML前置元数据解析、
Mermaid图表支持等功能。

许可证: MIT License
适用范围: 核心Markdown处理功能、Web应用
注意: 桌面应用模块使用GPL v3许可证（由于PyQt5依赖）

作者: LAD Markdown Viewer Contributors
版本: 1.2.0
"""

__version__ = "1.3.0"
__author__ = "LAD Markdown Viewer Contributors"
__license__ = "MIT"
__description__ = "A powerful Markdown viewer with YAML front-matter and Mermaid support"

# 核心功能模块
from .markdown_processor import render_markdown_to_html
from .markdown_utils import extract_mermaid_blocks, restore_mermaid_blocks, slugify

__all__ = [
    'render_markdown_to_html',
    'extract_mermaid_blocks',
    'restore_mermaid_blocks',
    'slugify',
] 