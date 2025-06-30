# Windows开发环境一键配置脚本 v1.2
# 适用于通用Windows开发环境配置
# 支持AI配置文件v2.0和时间戳规范
# [⏰ 时间：2025-06-24 16:27]
# PowerShell版本兼容性：
#   最低要求：Windows PowerShell 5.1 或 PowerShell Core 6.0+
#   推荐版本：PowerShell 7.0+
#   测试环境：Windows PowerShell 5.1, PowerShell 7.x
#   已知限制：Windows PowerShell不支持&&和||操作符
# 功能说明：符合LAD项目AI配置v2.0规范，强制使用分号(;)作为命令分隔符

param(
    [switch]$SkipPowerShell,
    [switch]$SkipGit,
    [switch]$SkipAI,
    [switch]$SkipEditor,
    [switch]$Verify,
    [switch]$Force,
    [switch]$TimestampTest
)

# PowerShell版本兼容性检查
if ($PSVersionTable.PSVersion -lt [Version]"5.1") {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ❌ PowerShell版本过低" -ForegroundColor Red
    Write-Host "当前版本: $($PSVersionTable.PSVersion)" -ForegroundColor Yellow
    Write-Host "最低要求: 5.1" -ForegroundColor Yellow
    Write-Host "建议升级到PowerShell 7.0+" -ForegroundColor Cyan
    exit 1
}

# 设置错误处理
$ErrorActionPreference = "Continue"

# 显示当前时间戳（符合AI行为规则）
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 开始Windows开发环境配置..." -ForegroundColor Yellow

Write-Host "🚀 Windows开发环境一键配置 v1.1" -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Cyan
Write-Host "配置类型: 通用Windows开发环境" -ForegroundColor Yellow
Write-Host "支持功能: AI配置文件v2.0 + 时间戳规范" -ForegroundColor Gray
Write-Host "配置时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm')" -ForegroundColor Yellow
Write-Host ""

# 时间戳测试功能
if ($TimestampTest) {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 🧪 时间戳功能测试" -ForegroundColor Cyan
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ 时间戳格式正确" -ForegroundColor Green
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 📋 时间戳规范验证通过" -ForegroundColor Green
    return
}

$configResults = @{
    "PowerShell编码配置" = $false
    "Git环境配置" = $false
    "AI工具配置" = $false
    "代码编辑器配置" = $false
    "环境验证" = $false
    "时间戳规范配置" = $false
}

# 1. PowerShell UTF-8编码配置
if (-not $SkipPowerShell) {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 🔧 1. 配置PowerShell UTF-8编码..." -ForegroundColor Green
    
    try {
        # 立即设置编码
        [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
        [Console]::InputEncoding = [System.Text.Encoding]::UTF8
        $PSDefaultParameterValues['*:Encoding'] = 'utf8'
        
        # 创建PowerShell配置文件
        $profileDir = Split-Path $PROFILE
        if (!(Test-Path $profileDir)) {
            New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
            Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ 创建PowerShell配置目录" -ForegroundColor Green
        }
        
        $profileContent = @"
# Windows开发环境PowerShell UTF-8编码配置 v1.1
# 支持AI配置文件v2.0和时间戳规范
# [⏰ 时间：$(Get-Date -Format "yyyy-MM-dd HH:mm")]

# 设置控制台编码为UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8

# 设置PowerShell默认编码为UTF-8
`$PSDefaultParameterValues['*:Encoding'] = 'utf8'

# Git环境变量（解决分页器问题）
`$env:GIT_PAGER = "cat"

# LAD时间戳函数 v2.0 - 增强版（符合AI配置v2.0规范）
function Get-LADTimestamp {
    param(
        [switch]$TimeOnly,  # 只返回时间字符串
        [switch]$Raw        # 返回原始Get-Date对象
    )
    
    if ($Raw) {
        return Get-Date
    } elseif ($TimeOnly) {
        return Get-Date -Format 'yyyy-MM-dd HH:mm'
    } else {
    return "[⏰ 时间：`$(Get-Date -Format 'yyyy-MM-dd HH:mm')]"
    }
}

# AI配置文件v2.0验证函数
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

Write-Host "`$(Get-LADTimestamp) Windows开发环境PowerShell UTF-8编码配置v1.1已加载" -ForegroundColor Green
Test-AIConfigV2
"@
        
        if ((Test-Path $PROFILE) -and !$Force) {
            Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ⚠️  PowerShell配置文件已存在，使用 -Force 参数覆盖" -ForegroundColor Yellow
            Write-Host "   📄 现有配置文件: $PROFILE" -ForegroundColor Cyan
        } else {
            $profileContent | Out-File $PROFILE -Encoding UTF8
            Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ PowerShell配置文件已创建: $PROFILE" -ForegroundColor Green
        }
        
        # 测试编码设置
        $testString = "测试中文编码：Windows开发环境v1.1"
        Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 🧪 编码测试: $testString" -ForegroundColor Cyan
        
        $configResults["PowerShell编码配置"] = $true
        
    } catch {
        Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ❌ PowerShell编码配置失败: $($_.Exception.Message)" -ForegroundColor Red
    }
} else {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ⏭️  跳过PowerShell编码配置" -ForegroundColor Yellow
}

# 2. Git环境配置
if (-not $SkipGit) {
    Write-Host "`n[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 📁 2. 配置Git环境..." -ForegroundColor Green
    
    try {
        # 检查Git是否安装
        $gitVersion = git --version 2>$null
        if ($LASTEXITCODE -ne 0) {
            Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ⚠️  Git未安装，跳过Git配置" -ForegroundColor Yellow
            Write-Host "   💡 请先安装Git: https://git-scm.com/" -ForegroundColor Cyan
        } else {
            Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ℹ️  检测到Git版本: $gitVersion" -ForegroundColor Cyan
            
            # Git全局配置
            git config --global core.pager cat
            git config --global core.quotepath false
            git config --global gui.encoding utf-8
            git config --global i18n.commit.encoding utf-8
            git config --global i18n.logoutputencoding utf-8
            
            Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ Git编码和分页器配置完成" -ForegroundColor Green
            
            # 检查Git用户信息
            $gitUser = git config --global user.name 2>$null
            $gitEmail = git config --global user.email 2>$null
            
            if (-not $gitUser -or -not $gitEmail) {
                Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ⚠️  Git用户信息未配置，请手动设置:" -ForegroundColor Yellow
                Write-Host "      git config --global user.name `"你的姓名`"" -ForegroundColor Cyan
                Write-Host "      git config --global user.email `"你的邮箱`"" -ForegroundColor Cyan
            } else {
                Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ Git用户信息: $gitUser <$gitEmail>" -ForegroundColor Green
            }
            
            $configResults["Git环境配置"] = $true
        }
        
    } catch {
        Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ❌ Git配置失败: $($_.Exception.Message)" -ForegroundColor Red
    }
} else {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ⏭️  跳过Git环境配置" -ForegroundColor Yellow
}

# 3. AI工具配置（支持v2.0和时间戳规范）
if (-not $SkipAI) {
    Write-Host "`n[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 🤖 3. 配置AI工具v2.0..." -ForegroundColor Green
    
    try {
        $aiConfig = @{
            "version" = "2.0"
            "project_type" = "通用Windows开发环境"
            "environment" = "windows-powershell"
            "command_separator" = ";"
            "forbidden_operators" = @("&&", "||")
            "preferred_syntax" = "powershell"
            "validation_rules" = @(
                "no-bash-operators",
                "powershell-compatible",
                "semicolon-separator",
                "timestamp-required"
            )
            "ai_behavior_rules" = @{
                "时间戳规范" = @{
                    "强制要求" = "每次回复开头包含[⏰ 时间：YYYY-MM-DD HH:mm]"
                    "获取方法" = "Get-Date -Format 'yyyy-MM-dd HH:mm'"
                    "验证机制" = "检查时间戳格式和时效性"
                    "误差容忍" = "5分钟内"
                }
                "命令输出规则" = "始终使用分号(;)作为命令分隔符"
                "条件执行规则" = "使用if语句和`$LASTEXITCODE检查"
                "语法兼容性" = "确保所有命令与PowerShell 5.1+兼容"
                "路径格式" = "使用Windows路径分隔符或PowerShell兼容路径"
            }
            "timestamp_config" = @{
                "format" = "yyyy-MM-dd HH:mm"
                "prefix" = "[⏰ 时间："
                "suffix" = "]"
                "validation_enabled" = $true
                "auto_update" = $true
            }
            "created_time" = (Get-LADTimestamp -TimeOnly)
            "created_by" = "Windows开发环境配置脚本 v1.1"
            "last_updated" = (Get-LADTimestamp -TimeOnly)
        } | ConvertTo-Json -Depth 4
        
        if ((Test-Path ".ai-config.json") -and !$Force) {
            Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ⚠️  AI配置文件已存在，使用 -Force 参数覆盖" -ForegroundColor Yellow
        } else {
            $aiConfig | Out-File ".ai-config.json" -Encoding UTF8
            Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ AI配置文件v2.0已创建: .ai-config.json" -ForegroundColor Green
        }
        
        # 创建AI提示词文件
        $aiPrompt = @"
# Windows开发环境AI助手配置提示词 v1.1
# 支持AI配置文件v2.0和时间戳规范
# [⏰ 时间：$(Get-Date -Format "yyyy-MM-dd HH:mm")]

## 核心要求
**每次回复都必须以时间戳开头：[⏰ 时间：YYYY-MM-DD HH:mm]**

## 环境信息
- 操作系统：Windows 10/11
- Shell环境：PowerShell 5.1+
- 编码标准：UTF-8
- AI配置版本：v2.0

## 时间戳规范
1. **强制要求**：每次回复开头包含实时时间戳
2. **获取方法**：使用PowerShell命令 `Get-Date -Format "yyyy-MM-dd HH:mm"`
3. **格式标准**：[⏰ 时间：YYYY-MM-DD HH:mm]
4. **验证机制**：检查时间戳格式和时效性（5分钟误差容忍）

## 命令输出规则
1. **命令分隔符**：使用分号(;)，禁止使用&&
2. **条件执行**：使用if语句和`$LASTEXITCODE检查
3. **语法兼容**：确保所有命令与PowerShell兼容
4. **路径格式**：使用Windows路径分隔符

## 示例转换
- ❌ 错误：git add . && git commit -m "msg"
- ✅ 正确：git add .; git commit -m "msg"
- 🌟 更好：git add .; if (`$LASTEXITCODE -eq 0) { git commit -m "msg" }

## 时间戳示例
- ✅ 正确：[⏰ 时间：2025-06-24 11:54] 开始执行配置...
- ❌ 错误：[时间：2025-06-24] 或 没有时间戳

请在所有回复中严格遵循这些规则，特别是时间戳要求。
"@
        
        if (!(Test-Path "ai-prompt-template.md") -or $Force) {
            $aiPrompt | Out-File "ai-prompt-template.md" -Encoding UTF8
            Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ AI提示词模板v1.1已创建: ai-prompt-template.md" -ForegroundColor Green
        }
        
        Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 📋 请在AI会话开始时使用ai-prompt-template.md中的提示词" -ForegroundColor Cyan
        
        $configResults["AI工具配置"] = $true
        $configResults["时间戳规范配置"] = $true
        
    } catch {
        Write-Host "   [⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ❌ AI配置失败: $($_.Exception.Message)" -ForegroundColor Red
    }
} else {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ⏭️  跳过AI工具配置" -ForegroundColor Yellow
}

# 4. 代码编辑器配置
if (-not $SkipEditor) {
    Write-Host "`n🎯 4. 配置代码编辑器..." -ForegroundColor Green
    
    try {
        # 创建VS Code配置目录
        $vscodeDir = ".vscode"
        if (!(Test-Path $vscodeDir)) {
            New-Item -ItemType Directory -Path $vscodeDir -Force | Out-Null
            Write-Host "   ✅ 创建VS Code配置目录" -ForegroundColor Green
        }
        
        # VS Code settings.json
        $vscodeSettings = @{
            "terminal.integrated.defaultProfile.windows" = "PowerShell"
            "terminal.integrated.profiles.windows" = @{
                "PowerShell" = @{
                    "source" = "PowerShell"
                    "args" = @("-NoProfile")
                }
            }
            "files.encoding" = "utf8"
            "files.autoGuessEncoding" = $true
            "git.enableSmartCommit" = $true
            "git.confirmSync" = $false
            "editor.formatOnSave" = $true
            "powershell.integratedConsole.showOnStartup" = $false
        } | ConvertTo-Json -Depth 4
        
        if (!(Test-Path "$vscodeDir/settings.json") -or $Force) {
            $vscodeSettings | Out-File "$vscodeDir/settings.json" -Encoding UTF8
            Write-Host "   ✅ VS Code配置已创建" -ForegroundColor Green
        }
        
        # Cursor配置
        $cursorrules = @"
# Windows开发环境Cursor配置
# [⏰ 时间：$(Get-Date -Format "yyyy-MM-dd HH:mm")]

## 环境设定
- 操作系统：Windows
- Shell：PowerShell
- 编码：UTF-8

## 代码规范
1. **PowerShell脚本**：
   - 使用UTF-8编码
   - 详细的错误处理
   - 用户友好的输出格式

2. **Python代码**：
   - 遵循PEP 8规范
   - 使用类型注解
   - UTF-8编码处理

## 命令输出规范
- 使用分号(;)作为PowerShell命令分隔符
- 禁止使用Bash风格的&&和||操作符
- 使用PowerShell原生的条件执行语法
"@
        
        if (!(Test-Path ".cursorrules") -or $Force) {
            $cursorrules | Out-File ".cursorrules" -Encoding UTF8
            Write-Host "   ✅ Cursor配置已创建" -ForegroundColor Green
        }
        
        # 创建编辑器配置说明
        $editorReadme = @"
# Windows开发环境编辑器配置说明

## 配置文件
- **.vscode/settings.json** - VS Code项目配置
- **.cursorrules** - Cursor开发规则
- **ai-prompt-template.md** - AI助手配置提示词

## VS Code配置要点
- 默认终端：PowerShell
- 文件编码：UTF-8
- 自动格式化：开启
- Git集成：优化设置

## Cursor配置要点
- PowerShell命令兼容性
- UTF-8编码标准
- 代码规范约束

## 使用建议
1. 重启编辑器使配置生效
2. 在AI会话中使用提示词模板
3. 验证终端编码设置
4. 测试Git集成功能
"@
        
        if (!(Test-Path "editor-config-readme.md") -or $Force) {
            $editorReadme | Out-File "editor-config-readme.md" -Encoding UTF8
            Write-Host "   ✅ 编辑器配置说明已创建" -ForegroundColor Green
        }
        
        $configResults["代码编辑器配置"] = $true
        
    } catch {
        Write-Host "   ❌ 代码编辑器配置失败: $($_.Exception.Message)" -ForegroundColor Red
    }
} else {
    Write-Host "⏭️  跳过代码编辑器配置" -ForegroundColor Yellow
}

# 5. 环境验证
if ($Verify) {
    Write-Host "`n🔍 5. 验证配置..." -ForegroundColor Green
    
    try {
        $verificationResults = @{}
        
        # 验证PowerShell编码
        $outputEncoding = [Console]::OutputEncoding.EncodingName
        $inputEncoding = [Console]::InputEncoding.EncodingName
        
        if ($outputEncoding -like "*UTF*" -and $inputEncoding -like "*UTF*") {
            Write-Host "   ✅ PowerShell编码: $outputEncoding / $inputEncoding" -ForegroundColor Green
            $verificationResults["PowerShell编码"] = "正常"
        } else {
            Write-Host "   ❌ PowerShell编码异常: $outputEncoding / $inputEncoding" -ForegroundColor Red
            $verificationResults["PowerShell编码"] = "异常"
        }
        
        # 验证Git配置
        if (Get-Command git -ErrorAction SilentlyContinue) {
            $gitPager = git config --global core.pager 2>$null
            if ($gitPager -eq "cat") {
                Write-Host "   ✅ Git分页器已禁用" -ForegroundColor Green
                $verificationResults["Git分页器"] = "正常"
            } else {
                Write-Host "   ❌ Git分页器配置异常: $gitPager" -ForegroundColor Red
                $verificationResults["Git分页器"] = "异常"
            }
            
            $gitQuotePath = git config --global core.quotepath 2>$null
            if ($gitQuotePath -eq "false") {
                Write-Host "   ✅ Git中文路径支持已启用" -ForegroundColor Green
                $verificationResults["Git中文支持"] = "正常"
            } else {
                Write-Host "   ❌ Git中文路径配置异常" -ForegroundColor Red
                $verificationResults["Git中文支持"] = "异常"
            }
        } else {
            Write-Host "   ⚠️  Git未安装，跳过验证" -ForegroundColor Yellow
            $verificationResults["Git配置"] = "未安装"
        }
        
        # 验证AI配置
        if (Test-Path ".ai-config.json") {
            try {
                $aiConf = Get-Content ".ai-config.json" -Raw | ConvertFrom-Json
                if ($aiConf.command_separator -eq ";") {
                    Write-Host "   ✅ AI配置正确：命令分隔符为分号" -ForegroundColor Green
                    $verificationResults["AI配置"] = "正常"
                } else {
                    Write-Host "   ❌ AI配置异常：命令分隔符不是分号" -ForegroundColor Red
                    $verificationResults["AI配置"] = "异常"
                }
            } catch {
                Write-Host "   ❌ AI配置文件格式错误" -ForegroundColor Red
                $verificationResults["AI配置"] = "格式错误"
            }
        } else {
            Write-Host "   ⚠️  AI配置文件不存在" -ForegroundColor Yellow
            $verificationResults["AI配置"] = "不存在"
        }
        
        # 验证配置文件
        if (Test-Path $PROFILE) {
            Write-Host "   ✅ PowerShell配置文件存在" -ForegroundColor Green
            $verificationResults["配置文件"] = "存在"
        } else {
            Write-Host "   ❌ PowerShell配置文件不存在" -ForegroundColor Red
            $verificationResults["配置文件"] = "不存在"
        }
        
        # 生成验证报告
        $verificationReport = @{
            "验证时间" = (Get-Date -Format "yyyy-MM-dd HH:mm")
            "PowerShell版本" = $PSVersionTable.PSVersion.ToString()
            "验证结果" = $verificationResults
        } | ConvertTo-Json -Depth 3
        
        $verificationReport | Out-File "windows-dev-env-verification.json" -Encoding UTF8
        Write-Host "   📄 验证报告已保存: windows-dev-env-verification.json" -ForegroundColor Cyan
        
        $configResults["环境验证"] = $true
        
    } catch {
        Write-Host "   ❌ 验证过程出错: $($_.Exception.Message)" -ForegroundColor Red
    }
} else {
    Write-Host "⏭️  跳过环境验证（使用 -Verify 参数启用）" -ForegroundColor Yellow
}

# 输出配置总结
Write-Host "`n📊 配置结果总结" -ForegroundColor Cyan
Write-Host "=" * 40 -ForegroundColor Cyan

$successCount = 0
$totalCount = $configResults.Count

foreach ($item in $configResults.GetEnumerator()) {
    $status = if ($item.Value) { "✅"; $successCount++ } else { "❌" }
    Write-Host "$status $($item.Key)" -ForegroundColor $(if ($item.Value) { "Green" } else { "Red" })
}

$successRate = [math]::Round(($successCount / $totalCount) * 100, 1)
Write-Host "`n成功率: $successCount/$totalCount ($successRate%)" -ForegroundColor $(if ($successRate -ge 80) { "Green" } elseif ($successRate -ge 60) { "Yellow" } else { "Red" })

if ($successRate -ge 90) {
    Write-Host "🎉 Windows开发环境配置完成！环境状态优秀！" -ForegroundColor Green
} elseif ($successRate -ge 70) {
    Write-Host "✅ Windows开发环境配置基本完成，建议检查失败项目" -ForegroundColor Yellow
} else {
    Write-Host "⚠️  Windows开发环境配置存在问题，请检查错误信息" -ForegroundColor Red
}

Write-Host "`n📚 后续步骤:" -ForegroundColor Cyan
Write-Host "1. 重启PowerShell使配置生效：. `$PROFILE" -ForegroundColor White
Write-Host "2. 在AI会话中使用ai-prompt-template.md中的提示词" -ForegroundColor White
Write-Host "3. 测试Git命令：git status（如果已安装Git）" -ForegroundColor White
Write-Host "4. 测试中文显示：Write-Host '中文测试'" -ForegroundColor White
Write-Host "5. 查看配置文档：Windows开发环境一键配置指南.md" -ForegroundColor White

Write-Host "`n📁 创建的配置文件:" -ForegroundColor Cyan
$createdFiles = @(
    $PROFILE,
    ".ai-config.json",
    "ai-prompt-template.md",
    ".vscode/settings.json",
    ".cursorrules",
    "editor-config-readme.md"
)

foreach ($file in $createdFiles) {
    if (Test-Path $file) {
        Write-Host "   ✅ $file" -ForegroundColor Green
    }
}

if ($Verify -and (Test-Path "windows-dev-env-verification.json")) {
    Write-Host "   📄 windows-dev-env-verification.json" -ForegroundColor Cyan
}

Write-Host "`n🎊 欢迎使用优化后的Windows开发环境！" -ForegroundColor Green 