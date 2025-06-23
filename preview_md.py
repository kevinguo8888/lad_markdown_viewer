#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LAD MD文档预览工具
支持多种预览方式：Web浏览器、桌面应用、控制台输出
使用lad_markdown_viewer包进行Markdown处理
"""

import sys
import os
import webbrowser
import tempfile
from pathlib import Path

# 导入我们的Markdown处理包
from lad_markdown_viewer.markdown_processor import render_markdown_to_html

def preview_in_browser(md_file_path):
    """在浏览器中预览MD文档"""
    try:
        # 读取MD文件
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
        
        # 使用包中的渲染函数
        html_body = render_markdown_to_html(md_text)
        
        # 创建完整的HTML页面
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>MD预览 - {os.path.basename(md_file_path)}</title>
            <script src="https://cdn.jsdelivr.net/npm/mermaid@9.4.3/dist/mermaid.min.js"></script>
            <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    try {{
                        if (typeof mermaid !== 'undefined') {{
                            mermaid.initialize({{
                                startOnLoad: true,
                                theme: 'default',
                                securityLevel: 'loose',
                                flowchart: {{ htmlLabels: true, useMaxWidth: true }},
                            }});
                        }}
                    }} catch(e) {{
                        console.error('Mermaid initialization error:', e);
                    }}
                }});
            </script>
            <style>
                body {{ 
                    font-family: '微软雅黑', 'Microsoft YaHei', Arial, sans-serif; 
                    margin: 30px; 
                    line-height: 1.6; 
                    max-width: 1200px;
                    margin-left: auto;
                    margin-right: auto;
                }}
                table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
                th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
                th {{ background: #f6f8fa; }}
                pre {{ background: #f6f8fa; padding: 10px; border-radius: 4px; overflow-x: auto; }}
                code {{ background: #f6f8fa; padding: 2px 4px; border-radius: 4px; }}
                .mermaid {{ background: white; padding: 10px; border-radius: 4px; text-align: center; }}
                h1, h2, h3, h4, h5, h6 {{ color: #24292e; }}
                h1 {{ border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }}
                h2 {{ border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }}
                blockquote {{ border-left: 4px solid #dfe2e5; padding-left: 16px; color: #6a737d; }}
                img {{ max-width: 100%; height: auto; }}
                .yaml-metadata {{ margin-bottom: 20px; }}
                .toc {{ background: #f8f9fa; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
                .toc ul {{ margin: 0; padding-left: 20px; }}
                .toc li {{ margin: 5px 0; }}
                .toc a {{ text-decoration: none; color: #0366d6; }}
                .toc a:hover {{ text-decoration: underline; }}
            </style>
        </head>
        <body>
        {html_body}
        </body>
        </html>
        """
        
        # 创建临时HTML文件
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
            f.write(html)
            temp_file = f.name
        
        # 在浏览器中打开
        webbrowser.open(f'file://{temp_file}')
        print(f"✅ 已在浏览器中打开预览：{md_file_path}")
        print(f"📄 临时HTML文件：{temp_file}")
        
    except ImportError as e:
        print(f"❌ 导入错误：{e}")
        print("请确保已安装依赖：pip install mistune pyyaml")
        print("或者安装完整的lad_markdown_viewer包")
    except Exception as e:
        print(f"❌ 预览失败：{e}")

def preview_in_console(md_file_path):
    """在控制台输出MD内容"""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"\n{'='*60}")
        print(f"MD文档预览：{md_file_path}")
        print(f"{'='*60}")
        print(content)
        print(f"{'='*60}")
        
    except UnicodeEncodeError:
        # 处理Windows控制台编码问题
        try:
            with open(md_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print(f"\n{'='*60}")
            print(f"MD文档预览：{md_file_path}")
            print(f"{'='*60}")
            # 使用ASCII兼容的方式输出
            print(content.encode('utf-8', errors='replace').decode('utf-8', errors='replace'))
            print(f"{'='*60}")
        except Exception as e:
            print(f"读取文件失败：{e}")
    except Exception as e:
        print(f"读取文件失败：{e}")

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("LAD MD文档预览工具")
        print("=" * 40)
        print("使用方法：")
        print("  python preview_md.py <md文件路径> [--console]")
        print("")
        print("参数说明：")
        print("  <md文件路径>  要预览的Markdown文件路径")
        print("  --console     在控制台输出原始内容（可选）")
        print("")
        print("示例：")
        print("  python preview_md.py 发布检查清单.md")
        print("  python preview_md.py 发布检查清单.md --console")
        print("")
        print("功能特性：")
        print("  ✅ 支持YAML元信息自动表格化")
        print("  ✅ 支持目录自动生成和跳转")
        print("  ✅ 支持Mermaid图表渲染")
        print("  ✅ 支持表格、任务列表、代码高亮")
        print("  ✅ 支持数学公式、脚注等扩展语法")
        return
    
    md_file = sys.argv[1]
    
    if not os.path.exists(md_file):
        print(f"❌ 文件不存在：{md_file}")
        return
    
    if len(sys.argv) > 2 and sys.argv[2] == '--console':
        preview_in_console(md_file)
    else:
        preview_in_browser(md_file)

if __name__ == '__main__':
    main() 