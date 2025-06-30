# Windows开发环境一键配置指南

**文档版本**: v1.2  
**创建日期**: 2025-06-23  
**最后更新**: 2025-06-24 11:42  
**适用系统**: Windows 10/11  
**文档类型**: 通用配置指南  
**AI配置支持**: .ai-config.json v2.0

## 📋 文档概述

本指南提供Windows系统下完整的开发环境配置方案，适用于任何需要配置PowerShell、Git、AI工具、代码编辑器的开发项目。特别针对中文开发者优化，解决常见的编码、分页器、兼容性问题，并完全支持LAD贷顾问平台AI配置文件v2.0的时间戳规范要求。

## 🎯 适用场景

- **新电脑环境搭建**: 全新Windows系统的开发环境配置
- **多项目开发**: 通用的开发工具配置，适用于不同项目
- **团队标准化**: 建立团队统一的开发环境标准
- **问题修复**: 解决现有环境的常见问题
- **AI助手配置**: 确保AI工具遵循时间戳和命令兼容性规范
- **LAD项目支持**: 完整支持LAD贷顾问平台的AI配置文件v2.0

## 🚀 一键配置方案

### 快速配置（推荐）

```powershell
# 显示当前时间戳（符合AI行为规则）
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 开始配置Windows开发环境..."

# 下载并运行通用配置脚本
.\setup-windows-dev-env.ps1

# 或使用批处理版本
.\setup-windows-dev-env.bat
```

### 配置内容概览

| 配置模块 | 解决问题 | 效果 | AI配置v2.0支持 |
|---------|---------|------|---------------|
| **PowerShell UTF-8编码** | 中文乱码问题 | 中文正确显示 | ✅ 时间戳显示支持 |
| **Git分页器优化** | 命令卡死问题 | 流畅的Git操作 | ✅ 命令兼容性 |
| **AI工具配置v2.0** | 命令兼容性问题 | PowerShell兼容输出 | ✅ 完整规范支持 |
| **时间戳规范强化** | AI回复格式问题 | 统一的时间戳格式 | ✅ 实时验证机制 |
| **代码编辑器配置** | 开发体验问题 | 统一的开发环境 | ✅ 配置文件集成 |
| **环境验证** | 配置完整性问题 | 自动检查和修复 | ✅ AI配置验证 |

## 🔧 核心配置模块

### 1. PowerShell UTF-8编码配置 (v1.2强化)

#### 问题描述
Windows PowerShell默认使用GB2312编码，导致：
- 中文文件名显示乱码
- JSON配置文件中文内容错误
- Git提交信息编码异常
- 脚本输出中文字符异常
- **AI时间戳显示异常**（新增问题）

#### 完整解决方案

**立即生效配置**:
```powershell
# 显示配置开始时间戳
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 开始PowerShell UTF-8编码配置..."

# 设置控制台编码为UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8

# 设置PowerShell默认编码
$PSDefaultParameterValues['*:Encoding'] = 'utf8'

# 验证时间戳显示（支持LAD时间戳规范）
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] UTF-8编码配置完成" -ForegroundColor Green
```

**持久化配置（支持AI配置v2.0）**:
```powershell
# 检查PowerShell配置文件路径
$PROFILE

# 创建配置文件目录（如果不存在）
if (!(Test-Path (Split-Path $PROFILE))) {
    New-Item -ItemType Directory -Path (Split-Path $PROFILE) -Force
}

# 写入配置内容（包含AI配置v2.0支持）
@"
# Windows开发环境PowerShell UTF-8编码配置 v1.2
# [⏰ 时间：$(Get-Date -Format "yyyy-MM-dd HH:mm")]
# 支持AI配置文件: .ai-config.json v2.0

# 设置控制台编码为UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8

# 设置PowerShell默认编码为UTF-8
`$PSDefaultParameterValues['*:Encoding'] = 'utf8'

# Git环境变量（解决分页器问题）
`$env:GIT_PAGER = "cat"

# LAD项目时间戳辅助函数（符合AI配置v2.0规范）
function Get-LADTimestamp {
    return "[⏰ 时间：`$(Get-Date -Format 'yyyy-MM-dd HH:mm')]"
}

# AI配置文件验证函数
function Test-AIConfigV2 {
    if (Test-Path ".ai-config.json") {
        try {
            `$config = Get-Content ".ai-config.json" | ConvertFrom-Json
            if (`$config.version -eq "2.0") {
                Write-Host "`$(Get-LADTimestamp) AI配置文件v2.0验证通过" -ForegroundColor Green
                return `$true
            }
        } catch {
            Write-Host "`$(Get-LADTimestamp) AI配置文件格式错误" -ForegroundColor Red
        }
    }
    Write-Host "`$(Get-LADTimestamp) 未发现AI配置文件v2.0" -ForegroundColor Yellow
    return `$false
}

Write-Host "`$(Get-LADTimestamp) Windows开发环境PowerShell UTF-8编码配置已加载" -ForegroundColor Green
Test-AIConfigV2
"@ | Out-File $PROFILE -Encoding UTF8
```

**验证方法（包含AI配置验证）**:
```powershell
# 检查编码设置
[Console]::OutputEncoding.EncodingName  # 应显示：Unicode (UTF-8)
[Console]::InputEncoding.EncodingName   # 应显示：Unicode (UTF-8)

# 测试中文显示
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 测试中文显示：Windows开发环境配置" -ForegroundColor Green

# 测试时间戳格式（AI配置v2.0规范）
$TimestampTest = "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 时间戳测试"
Write-Host $TimestampTest -ForegroundColor Yellow

# 验证时间戳格式正确性
if ($TimestampTest -match '^\[⏰ 时间：\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]') {
    Write-Host "✅ 时间戳格式符合AI配置v2.0规范" -ForegroundColor Green
} else {
    Write-Host "❌ 时间戳格式不符合规范" -ForegroundColor Red
}

# 测试JSON处理（包含时间戳）
$TestJson = @{
    "项目" = "Windows开发环境"
    "编码" = "UTF-8"
    "时间" = (Get-Date -Format 'yyyy-MM-dd HH:mm')
    "AI配置版本" = "v2.0"
} | ConvertTo-Json -Depth 3
Write-Host $TestJson
```

### 2. Git环境优化配置

#### 问题描述
Git在Windows PowerShell环境下的常见问题：
- Git命令卡在`(END)`分页器提示符
- 中文文件名和提交信息显示异常
- 按Ctrl+C后出现PowerShell解析错误

#### 完整解决方案

**Git全局配置**:
```powershell
# 禁用Git分页器
git config --global core.pager cat

# 修复中文编码问题
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8
git config --global i18n.logoutputencoding utf-8

# 设置用户信息（如果未设置）
git config --global user.name "你的姓名"
git config --global user.email "你的邮箱"
```

**验证配置**:
```powershell
# 检查Git配置
git config --global --list | Select-String -Pattern "(pager|encoding|quotepath|user)"

# 测试Git命令
git log --oneline -3  # 应该无分页器中断
git status           # 应该正常显示
```

### 3. AI工具配置

#### 问题描述
AI助手经常输出Bash风格的命令，在Windows PowerShell环境下不兼容：
- 使用`&&`和`||`操作符
- Unix风格的路径分隔符
- Bash特有的语法结构
- 忽略时间戳规范要求

#### 通用AI配置方案

**创建AI配置文件**:
```json
{
  "environment": "windows-powershell",
  "command_separator": ";",
  "forbidden_operators": ["&&", "||"],
  "preferred_syntax": "powershell",
  "validation_rules": [
    "no-bash-operators",
    "powershell-compatible",
    "semicolon-separator",
    "timestamp-required"
  ],
  "ai_behavior_rules": {
    "时间戳规范": "每次回复开头必须包含[⏰ 时间：YYYY-MM-DD HH:mm]",
    "时间获取方法": "使用Get-Date -Format 'yyyy-MM-dd HH:mm'",
    "命令输出规则": "始终使用分号(;)作为命令分隔符",
    "条件执行规则": "使用if语句和$LASTEXITCODE检查",
    "语法兼容性": "确保所有命令与PowerShell 5.1+兼容",
    "错误处理": "使用PowerShell原生错误处理机制",
    "中文回复": "所有回复必须使用中文"
  },
  "created_time": "2025-06-24 10:03"
}
```

**AI会话配置提示词**:
```
# Windows开发环境AI助手配置
## 环境信息
- 操作系统：Windows 10/11
- Shell环境：PowerShell 5.1+
- 编码标准：UTF-8

## AI行为规则（必须遵循）
1. **时间戳要求**：每次回复开头必须包含[⏰ 时间：YYYY-MM-DD HH:mm]
2. **获取时间方法**：使用PowerShell命令 Get-Date -Format "yyyy-MM-dd HH:mm"
3. **命令分隔符**：使用分号(;)，禁止使用&&
4. **条件执行**：使用if语句和$LASTEXITCODE检查
5. **语法兼容**：确保所有命令与PowerShell兼容
6. **路径格式**：使用Windows路径分隔符或PowerShell兼容路径
7. **中文回复**：所有回复必须使用中文

## 示例转换
- ❌ 错误：`git add . && git commit -m "msg"`
- ✅ 正确：`git add .; git commit -m "msg"`
- 🌟 更好：`git add .; if ($LASTEXITCODE -eq 0) { git commit -m "msg" }`
- 📅 时间戳：`[⏰ 时间：2025-06-24 10:03] 开始执行任务...`

请在所有回复中严格遵循这些规则。
```

### 4. 代码编辑器配置

#### VS Code配置

**settings.json**:
```json
{
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "source": "PowerShell",
      "args": ["-NoProfile"]
    }
  },
  "files.encoding": "utf8",
  "files.autoGuessEncoding": true,
  "[powershell]": {
    "files.encoding": "utf8bom"
  },
  "git.terminalAuthentication": false,
  "terminal.integrated.env.windows": {
    "GIT_PAGER": "cat"
  }
}
```

#### Cursor配置

**.cursorrules**:
```markdown
# Windows开发环境Cursor配置

## 环境信息
- 操作系统：Windows 10/11
- Shell：PowerShell 5.1+
- 编码：UTF-8

## AI行为规则
1. 时间戳要求：每次回复开头必须包含[⏰ 时间：YYYY-MM-DD HH:mm]
2. 命令分隔符：使用分号(;)，禁止使用&&操作符
3. 语法兼容：确保所有命令与PowerShell兼容
4. 中文支持：正确处理中文编码和显示

## 开发规范
- PowerShell脚本使用UTF-8编码
- 文件命名使用英文或合规的中文
- 所有配置文件使用UTF-8编码
```

## 🧪 配置验证

### 验证脚本
```powershell
# test-environment.ps1
Write-Host "=== Windows开发环境配置验证 ===" -ForegroundColor Cyan
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 开始验证..." -ForegroundColor Yellow

# 1. PowerShell编码验证
Write-Host "`n1. PowerShell编码验证:" -ForegroundColor Green
Write-Host "  输出编码: $([Console]::OutputEncoding.EncodingName)"
Write-Host "  输入编码: $([Console]::InputEncoding.EncodingName)"

# 2. Git配置验证
Write-Host "`n2. Git配置验证:" -ForegroundColor Green
$gitPager = git config --global --get core.pager
$gitQuotepath = git config --global --get core.quotepath
Write-Host "  Git分页器: $gitPager"
Write-Host "  Git quotepath: $gitQuotepath"

# 3. 中文显示测试
Write-Host "`n3. 中文显示测试:" -ForegroundColor Green
Write-Host "  中文测试：Windows开发环境配置 ✅"

# 4. 时间戳格式测试
Write-Host "`n4. 时间戳格式测试:" -ForegroundColor Green
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
Write-Host "  标准格式：[⏰ 时间：$timestamp]"

# 5. JSON中文处理测试
Write-Host "`n5. JSON中文处理测试:" -ForegroundColor Green
$testJson = @{
    "项目" = "Windows开发环境"
    "编码" = "UTF-8"
    "时间" = $timestamp
} | ConvertTo-Json -Depth 2
Write-Host "  JSON测试：$($testJson | ConvertFrom-Json | Select-Object -Property 项目)"

Write-Host "`n✅ 验证完成！" -ForegroundColor Green
```

## 🔗 相关资源

### LAD贷顾问平台集成
如果你在使用LAD贷顾问平台，可以参考以下专用配置：
- `D:\lad\LAD_Project\scripts\setup-lad-dev-env.ps1`
- `D:\lad\LAD_Project\07_Templates_Standards\02_Process_Standards\LAD-07-02-008_PowerShell中文编码配置指南_v1.0.md`
- `D:\lad\LAD_Project\07_Templates_Standards\05_Tool_Prompts\LAD-AI-PowerShell-Config-Prompt.md`

### 最佳实践
1. **统一编码标准**：所有项目文件使用UTF-8编码
2. **自动化配置**：使用脚本确保环境一致性
3. **验证机制**：定期检查配置有效性
4. **时间戳规范**：在AI交互中保持时间戳一致性
5. **文档同步**：保持配置文档与实际配置一致

---

## 🔄 版本历史

- **v1.0** (2025-06-23 18:20)：初始版本，建立Windows开发环境配置标准
- **v1.1** (2025-06-24 10:03)：增加时间戳规范支持、LAD项目集成说明、完善AI配置
- **v1.2** (2025-06-24 11:42)：强化时间戳规范、AI配置v2.0支持

---

**重要提醒**: 本配置指南提供了完整的Windows开发环境配置解决方案。正确配置后可以完美处理中文内容、Git操作和AI助手交互，支持现代开发工作流程和时间戳规范要求。

**最后更新**: 2025-06-24 11:42  
**下次审查**: 2025-07-24  
**状态**: 生效中 