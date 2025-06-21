#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LAD Markdown Viewer
一个功能强大的Markdown查看器，支持Web和桌面应用
"""

from setuptools import setup, find_packages
import os

# 读取README文件
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "LAD Markdown Viewer - 一个功能强大的Markdown查看器"

# 读取requirements文件
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return [
        'mistune>=2.0.0',
        'PyQt5>=5.15.0',
        'PyQtWebEngine>=5.15.0',
        'flask>=2.0.0',
        'pyyaml>=5.4.0',
    ]

setup(
    name='lad-markdown-viewer',
    version='1.2.0',
    author='LAD Markdown Viewer Contributors',
    author_email='support@lad-markdown-viewer.org',
    description='一个功能强大的Markdown查看器，支持Web和桌面应用',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/lad-markdown-viewer/lad-markdown-viewer',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Text Processing :: Markup',
        'Topic :: Software Development :: Documentation',
        'Topic :: Desktop Environment',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires='>=3.7',
    install_requires=read_requirements(),
    extras_require={
        'dev': [
            'pytest>=6.0.0',
            'pytest-cov>=2.10.0',
            'pytest-html>=3.0.0',
            'black>=21.0.0',
            'flake8>=3.8.0',
            'mypy>=0.800',
        ],
        'web': [
            'flask>=2.0.0',
            'flask-cors>=3.0.0',
        ],
        'desktop': [
            'PyQt5>=5.15.0',
            'PyQtWebEngine>=5.15.0',
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
        'lad_markdown_viewer': [
            '*.md',
            '*.txt',
            '*.html',
        ],
    },
    keywords=[
        'markdown',
        'viewer',
        'renderer',
        'html',
        'desktop',
        'web',
        'gui',
        'qt',
        'flask',
        'mermaid',
        'yaml',
        'toc',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/lad-markdown-viewer/lad-markdown-viewer/issues',
        'Source': 'https://github.com/lad-markdown-viewer/lad-markdown-viewer',
        'Documentation': 'https://github.com/lad-markdown-viewer/lad-markdown-viewer/blob/main/README.md',
        'Changelog': 'https://github.com/lad-markdown-viewer/lad-markdown-viewer/blob/main/CHANGELOG.md',
    },
    license='MIT',
    platforms=['any'],
    zip_safe=False,
) 