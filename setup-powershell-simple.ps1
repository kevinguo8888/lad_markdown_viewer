# PowerShell 环境快速配置脚本 v1.2
# 支持时间戳规范和AI配置文件v2.0
# [⏰ 时间：2025-06-24 16:27]
# PowerShell版本兼容性：
#   最低要求：Windows PowerShell 5.1 或 PowerShell Core 6.0+
#   推荐版本：PowerShell 7.0+
#   测试环境：Windows PowerShell 5.1, PowerShell 7.x
#   已知限制：Windows PowerShell不支持&&和||操作符
# 功能说明：符合LAD项目AI配置v2.0规范，强制使用分号(;)作为命令分隔符

param(
    [switch]$TestOnly,
    [switch]$ShowConfig
)

# PowerShell版本兼容性检查
if ($PSVersionTable.PSVersion -lt [Version]"5.1") {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ❌ PowerShell版本过低" -ForegroundColor Red
    Write-Host "当前版本: $($PSVersionTable.PSVersion)" -ForegroundColor Yellow
    Write-Host "最低要求: 5.1" -ForegroundColor Yellow
    Write-Host "建议升级到PowerShell 7.0+" -ForegroundColor Cyan
    exit 1
}

# 显示当前时间戳（符合AI行为规则）
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 开始PowerShell环境配置..." -ForegroundColor Yellow

Write-Host "🚀 LAD PowerShell 环境优化配置 v1.1" -ForegroundColor Cyan
Write-Host "支持AI配置文件v2.0和时间戳规范" -ForegroundColor Gray
Write-Host "========================================" -ForegroundColor Cyan

if ($ShowConfig) {
    Write-Host "`n📋 当前Git配置:" -ForegroundColor White
    Write-Host "  core.pager: $(git config --global --get core.pager)" -ForegroundColor Yellow
    Write-Host "  core.quotepath: $(git config --global --get core.quotepath)" -ForegroundColor Yellow
    Write-Host "  gui.encoding: $(git config --global --get gui.encoding)" -ForegroundColor Yellow
    
    Write-Host "`n📋 PowerShell配置:" -ForegroundColor White
    Write-Host "  配置文件路径: $PROFILE" -ForegroundColor Yellow
    Write-Host "  配置文件存在: $(Test-Path $PROFILE)" -ForegroundColor Yellow
    
    Write-Host "`n📋 编码设置:" -ForegroundColor White
    Write-Host "  输出编码: $([Console]::OutputEncoding.EncodingName)" -ForegroundColor Yellow
    Write-Host "  输入编码: $([Console]::InputEncoding.EncodingName)" -ForegroundColor Yellow
    
    # 检查AI配置文件v2.0
    Write-Host "`n📋 AI配置文件:" -ForegroundColor White
    if (Test-Path ".ai-config.json") {
        try {
            $config = Get-Content ".ai-config.json" | ConvertFrom-Json
            Write-Host "  配置文件存在: ✅" -ForegroundColor Green
            Write-Host "  版本: $($config.version)" -ForegroundColor Yellow
            if ($config.version -eq "2.0") {
                Write-Host "  时间戳规范支持: ✅" -ForegroundColor Green
            }
        } catch {
            Write-Host "  配置文件格式错误: ❌" -ForegroundColor Red
        }
    } else {
        Write-Host "  配置文件存在: ❌" -ForegroundColor Red
    }
    
    return
}

# 测试当前配置
function Test-CurrentConfig {
    $issues = @()
    
    # 检查Git分页器
    $pager = git config --global --get core.pager
    if ($pager -ne "cat") {
        $issues += "Git分页器未配置或配置错误"
    }
    
    # 检查Git编码
    $quotepath = git config --global --get core.quotepath
    if ($quotepath -ne "false") {
        $issues += "Git quotepath未配置"
    }
    
    # 检查PowerShell配置文件
    if (!(Test-Path $PROFILE)) {
        $issues += "PowerShell配置文件不存在"
    }
    
    # 检查AI配置文件v2.0
    if (!(Test-Path ".ai-config.json")) {
        $issues += "AI配置文件不存在"
    } else {
        try {
            $config = Get-Content ".ai-config.json" | ConvertFrom-Json
            if ($config.version -ne "2.0") {
                $issues += "AI配置文件版本不是v2.0"
            }
        } catch {
            $issues += "AI配置文件格式错误"
        }
    }
    
    return $issues
}

$issues = Test-CurrentConfig

if ($TestOnly) {
    Write-Host "`n🧪 测试当前配置..." -ForegroundColor Yellow
    if ($issues.Count -eq 0) {
        Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ 所有配置都正确！" -ForegroundColor Green
    } else {
        Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ❌ 发现以下问题:" -ForegroundColor Red
        foreach ($issue in $issues) {
            Write-Host "  - $issue" -ForegroundColor Red
        }
    }
    return
}

# 执行配置
Write-Host "`n[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 📋 开始配置..." -ForegroundColor Yellow

# 1. 配置Git
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 配置Git设置..." -ForegroundColor Yellow
git config --global core.pager cat
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8
git config --global i18n.logoutputencoding utf-8
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ Git配置完成" -ForegroundColor Green

# 2. 创建PowerShell配置文件
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 创建PowerShell配置文件..." -ForegroundColor Yellow

$profileDir = Split-Path $PROFILE
if (!(Test-Path $profileDir)) {
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
}

# 增强的配置内容（支持时间戳规范）
$configLines = @(
    "# LAD PowerShell 优化配置 v1.1 - $(Get-Date -Format 'yyyy-MM-dd HH:mm')",
    "# 支持AI配置文件v2.0和时间戳规范",
    "",
    "# 编码设置",
    "try {",
    "    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8",
    "    [Console]::InputEncoding = [System.Text.Encoding]::UTF8",
    "    `$PSDefaultParameterValues['*:Encoding'] = 'utf8'",
    "} catch { }",
    "",
    "# Git环境变量",
    "`$env:GIT_PAGER = 'cat'",
    "",
    "# LAD项目时间戳辅助函数（符合AI配置v2.0规范）",
    "function Get-LADTimestamp {",
    "    return `"[⏰ 时间：`$(Get-Date -Format 'yyyy-MM-dd HH:mm')]`"",
    "}",
    "",
    "# AI配置文件验证函数",
    "function Test-AIConfigV2 {",
    "    if (Test-Path `".ai-config.json`") {",
    "        try {",
    "            `$config = Get-Content `".ai-config.json`" | ConvertFrom-Json",
    "            if (`$config.version -eq `"2.0`") {",
    "                Write-Host `"`$(Get-LADTimestamp) AI配置文件v2.0验证通过`" -ForegroundColor Green",
    "                return `$true",
    "            }",
    "        } catch {",
    "            Write-Host `"`$(Get-LADTimestamp) AI配置文件格式错误`" -ForegroundColor Red",
    "        }",
    "    }",
    "    Write-Host `"`$(Get-LADTimestamp) 未发现AI配置文件v2.0`" -ForegroundColor Yellow",
    "    return `$false",
    "}",
    "",
    "# 常用别名",
    "Set-Alias -Name ll -Value Get-ChildItem -Force -ErrorAction SilentlyContinue",
    "Set-Alias -Name grep -Value Select-String -Force -ErrorAction SilentlyContinue",
    "",
    "# 实用函数",
    "function Get-FirstFile {",
    "    param([string]`$Pattern)",
    "    `$files = Get-ChildItem `$Pattern -ErrorAction SilentlyContinue",
    "    if (`$files) { return `$files[0].FullName }",
    "    return `$null",
    "}",
    "",
    "function Install-WheelSafe {",
    "    param([string]`$DistPath = 'dist')",
    "    Write-Host `"`$(Get-LADTimestamp) 查找wheel文件...`" -ForegroundColor Cyan",
    "    `$wheelFile = Get-FirstFile `"`$DistPath/*.whl`"",
    "    if (`$wheelFile) {",
    "        Write-Host `"`$(Get-LADTimestamp) 找到wheel文件: `$wheelFile`" -ForegroundColor Green",
    "        pip install --dry-run `"`$wheelFile`"",
    "    } else {",
    "        Write-Host `"`$(Get-LADTimestamp) 在 `$DistPath 中未找到wheel文件`" -ForegroundColor Red",
    "    }",
    "}",
    "",
    "Write-Host `"`$(Get-LADTimestamp) ✅ LAD PowerShell优化配置v1.1已加载`" -ForegroundColor Green",
    "Test-AIConfigV2"
)

try {
    $configLines | Out-File -FilePath $PROFILE -Encoding UTF8
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ PowerShell配置文件已创建: $PROFILE" -ForegroundColor Green
} catch {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ❌ 创建PowerShell配置文件失败: $_" -ForegroundColor Red
}

# 3. 创建AI配置文件v2.0（如果不存在）
if (!(Test-Path ".ai-config.json")) {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 创建AI配置文件v2.0..." -ForegroundColor Yellow
    
    $aiConfig = @{
        "version" = "2.0"
        "project" = "LAD PowerShell环境配置"
        "environment" = "windows-powershell"
        "command_separator" = ";"
        "forbidden_operators" = @("&&", "||")
        "ai_behavior_rules" = @{
            "时间戳规范" = @{
                "强制要求" = "每次回复开头包含[⏰ 时间：YYYY-MM-DD HH:mm]"
                "获取方法" = "Get-Date -Format 'yyyy-MM-dd HH:mm'"
                "验证机制" = "检查时间戳格式和时效性"
            }
            "命令输出规则" = "使用分号(;)作为分隔符"
            "PowerShell集成" = "使用PowerShell原生语法"
        }
        "created_time" = (Get-Date -Format "yyyy-MM-dd HH:mm")
        "created_by" = "setup-powershell-simple.ps1 v1.1"
    }
    
    try {
        $aiConfig | ConvertTo-Json -Depth 4 | Out-File ".ai-config.json" -Encoding UTF8
        Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ✅ AI配置文件v2.0已创建" -ForegroundColor Green
    } catch {
        Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ❌ 创建AI配置文件失败: $_" -ForegroundColor Red
    }
}

# 4. 验证配置
Write-Host "`n[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 🧪 验证配置..." -ForegroundColor Yellow
$newIssues = Test-CurrentConfig

if ($newIssues.Count -eq 0) {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 🎉 所有配置已成功完成！" -ForegroundColor Green
    Write-Host "`n📋 后续步骤:" -ForegroundColor White
    Write-Host "1. 重启PowerShell 或 运行: . `$PROFILE" -ForegroundColor Yellow
    Write-Host "2. 测试配置: .\setup-powershell-simple.ps1 -TestOnly" -ForegroundColor Yellow
    Write-Host "3. 查看配置: .\setup-powershell-simple.ps1 -ShowConfig" -ForegroundColor Yellow
    Write-Host "4. 验证时间戳: Write-Host `"[⏰ 时间：`$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 测试`"" -ForegroundColor Yellow
} else {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] ❌ 仍有以下问题:" -ForegroundColor Red
    foreach ($issue in $newIssues) {
        Write-Host "  - $issue" -ForegroundColor Red
    }
}

Write-Host "`n💡 v1.1新特性:" -ForegroundColor Cyan
Write-Host "- 支持AI配置文件v2.0时间戳规范" -ForegroundColor White
Write-Host "- 新增LAD项目时间戳辅助函数" -ForegroundColor White
Write-Host "- 增强AI配置文件验证功能" -ForegroundColor White
Write-Host "- 所有输出都包含实时时间戳" -ForegroundColor White

Write-Host "`n[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] PowerShell环境配置完成" -ForegroundColor Green 