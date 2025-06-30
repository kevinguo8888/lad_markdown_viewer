# Cursor AI Windows PowerShell环境专用配置

**模板版本**: v1.1  
**创建日期**: 2025-06-23  
**最后更新**: 2025-06-24 18:20  
**适用AI**: Cursor AI (内置AI助手)  
**环境**: Windows 10/11 + PowerShell 5.1+ + Cursor编辑器  
**优化特性**: Cursor编辑器集成优化 + 时间戳规范支持  
**AI配置支持**: .ai-config.json v2.0

---

## 🕐 Cursor AI专用Windows环境配置（时间戳规范版）

### 重要说明 🚨
Cursor AI，作为Cursor编辑器的内置AI助手，你在Windows PowerShell环境下工作时需要特别注意与编辑器的集成和命令兼容性。**同时必须严格遵循时间戳规范要求**。请严格遵循以下配置规则。

### 环境详细信息
- **操作系统**: Windows 10/11
- **Shell环境**: PowerShell 5.1 或 PowerShell 7+
- **编辑器**: Cursor (VS Code fork)
- **终端集成**: Cursor内置终端
- **编码标准**: UTF-8（中文环境）
- **命令分隔符**: 分号(`;`) **绝对不是** `&&`
- **时间戳规范**: 每次回复开头必须包含 `[⏰ 时间：YYYY-MM-DD HH:mm]`

### 🎯 核心AI行为规则（必须遵循）

#### 1. 强制时间戳规范
```powershell
# ✅ 每次回复开头都要包含实时时间戳
[⏰ 时间：2025-06-24 11:42] 开始Cursor工作区配置...

# ✅ 获取实时时间的正确方法
$CurrentTime = Get-Date -Format "yyyy-MM-dd HH:mm"
Write-Host "[⏰ 时间：$CurrentTime] 任务完成"

# ❌ 错误：缺少时间戳或使用历史日期
开始配置...  # 缺少时间戳
[⏰ 时间：2025-01-27 14:25] 任务...  # 历史日期错误示例

# ✅ 正确：使用实时时间戳
$CurrentTime = Get-Date -Format "yyyy-MM-dd HH:mm"
Write-Host "[⏰ 时间：$CurrentTime] 正在配置Cursor环境..."
```

#### 2. AI配置文件v2.0集成
```powershell
# Cursor AI应该识别和使用AI配置文件v2.0
function Test-CursorAIConfig {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 检查AI配置文件..." -ForegroundColor Cyan
    
    if (Test-Path ".ai-config.json") {
        try {
            $config = Get-Content ".ai-config.json" | ConvertFrom-Json
            if ($config.version -eq "2.0") {
                Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] AI配置v2.0验证通过" -ForegroundColor Green
                return $true
            }
        } catch {
            Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] AI配置文件格式错误" -ForegroundColor Red
        }
    }
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 未发现AI配置文件v2.0" -ForegroundColor Yellow
    return $false
}
```

### 🔧 Cursor AI特有问题和优化（v1.1更新）

#### 1. 编辑器集成命令（Cursor特色 + 时间戳）
```powershell
# ❌ 避免输出Unix风格的编辑器命令
code . && npm install && npm start

# ✅ Cursor AI应该输出（PowerShell + Cursor集成 + 时间戳）
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 启动Cursor项目..." -ForegroundColor Cyan
cursor .; npm install; npm start

# 🌟 Cursor AI推荐方式（利用编辑器功能 + 完整时间戳支持）
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 在Cursor编辑器中执行项目初始化..." -ForegroundColor Green
Set-Location $projectPath
npm install
if ($LASTEXITCODE -eq 0) {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 依赖安装成功，启动开发服务器..." -ForegroundColor Green
    npm start
} else {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 依赖安装失败，请检查package.json" -ForegroundColor Red
}
```

#### 2. Cursor工作区配置集成（支持AI配置v2.0）
```powershell
# Cursor AI可以生成工作区配置脚本（包含时间戳和AI配置v2.0支持）
function Initialize-CursorWorkspace {
    param(
        [string]$ProjectName,
        [string]$ProjectType = "general"
    )
    
    $CurrentTime = Get-Date -Format "yyyy-MM-dd HH:mm"
    Write-Host "[⏰ 时间：$CurrentTime] 初始化Cursor工作区: $ProjectName" -ForegroundColor Cyan
    
    # 创建项目目录
    New-Item -ItemType Directory -Name $ProjectName -Force
    Set-Location $ProjectName
    
    # 创建.cursor目录和配置
    New-Item -ItemType Directory -Name ".cursor" -Force
    
    # 生成Cursor工作区配置（集成AI配置v2.0规范）
    $cursorConfig = @{
        "ai_rules" = @{
            "environment" = "windows-powershell"
            "command_separator" = ";"
            "preferred_shell" = "powershell"
            "encoding" = "utf-8"
            "timestamp_required" = $true
            "timestamp_format" = "[⏰ 时间：YYYY-MM-DD HH:mm]"
            "ai_config_version" = "2.0"
        }
        "project_type" = $ProjectType
        "created_date" = $CurrentTime
        "cursor_integration" = @{
            "terminal_encoding" = "utf-8"
            "ai_behavior_rules" = @{
                "时间戳规范" = "每次回复开头必须包含实时时间戳"
                "命令分隔符" = "使用分号(;)而不是&&"
                "时间获取方法" = "Get-Date -Format 'yyyy-MM-dd HH:mm'"
            }
        }
    }
    
    $cursorConfig | ConvertTo-Json -Depth 4 | Out-File ".cursor/config.json" -Encoding UTF8
    
    # 创建AI配置文件v2.0
    $aiConfig = @{
        "version" = "2.0"
        "project" = $ProjectName
        "environment" = "windows-powershell-cursor"
        "command_separator" = ";"
        "forbidden_operators" = @("&&", "||")
        "ai_behavior_rules" = @{
            "时间戳规范" = @{
                "强制要求" = "每次回复开头包含[⏰ 时间：YYYY-MM-DD HH:mm]"
                "获取方法" = "Get-Date -Format 'yyyy-MM-dd HH:mm'"
                "验证机制" = "检查时间戳格式和时效性"
            }
            "命令输出规则" = "使用分号(;)作为分隔符"
            "Cursor集成" = "利用Cursor编辑器特性"
        }
        "created_time" = $CurrentTime
        "created_by" = "Cursor AI v1.1"
    }
    
    $aiConfig | ConvertTo-Json -Depth 4 | Out-File ".ai-config.json" -Encoding UTF8
    
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] Cursor工作区配置完成" -ForegroundColor Green
}
```

###  Cursor AI特定指令和集成

#### 1. 终端集成命令
```powershell
# Cursor AI应该了解Cursor编辑器的终端集成
function Invoke-CursorTerminal {
    param(
        [string]$Command,
        [switch]$NewTerminal
    )
    
    if ($NewTerminal) {
        Write-Host " 在新终端中执行: $Command" -ForegroundColor Cyan
        Start-Process powershell -ArgumentList "-NoExit", "-Command", $Command
    } else {
        Write-Host " 在当前终端中执行: $Command" -ForegroundColor Cyan
        Invoke-Expression $Command
    }
}
```

###  Cursor AI配置验证测试

请生成一个展示Cursor AI集成优势的PowerShell脚本，包含：
1. Cursor编辑器功能集成
2. 工作区配置管理
3. 终端命令优化
4. 调试配置生成
5. 扩展管理功能

---

##  Cursor AI确认清单

请确认你已理解并将严格遵循：

- [ ] 使用分号(`;`)分隔命令，绝不使用`&&`或`||`
- [ ] 充分利用Cursor编辑器的集成功能
- [ ] 生成Cursor工作区配置和调试设置
- [ ] 提供编辑器感知的PowerShell脚本
- [ ] 集成Cursor扩展管理功能
- [ ] 优化Cursor终端使用体验

**配置生效**: 立即生效，整个Cursor会话有效  
**验证方式**: 请生成一个Cursor集成的PowerShell项目管理脚本  
**特别优势**: 深度集成Cursor编辑器功能，提供一体化开发体验
