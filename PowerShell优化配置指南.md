# PowerShell 优化配置指南 v1.1

支持AI配置文件v2.0和时间戳规范  
[⏰ 时间：2025-06-24 11:54]

## 🎯 目标

解决在Windows PowerShell环境下开发时遇到的各种兼容性问题，特别是Git命令、编码问题和分页器问题。同时支持LAD项目的AI配置文件v2.0和时间戳规范要求。

## ❌ 常见问题

### 1. Git分页器问题
**问题表现**：
```powershell
git show commit_hash
# 输出显示 :...skipping... 和 (END)
# 按 Ctrl+C 后出现解析错误
```

**错误信息**：
```
: 无法将""项识别为 cmdlet、函数、脚本文件或可运行程序的名称
```

### 2. 通配符问题
**问题表现**：
```powershell
pip install --dry-run dist/*.whl
# ERROR: Invalid wheel filename (wrong number of parts): '*'
```

### 3. 命令连接问题
**问题表现**：
```powershell
git add file.txt && git commit -m "message"
# 标记"&&"不是此版本中的有效语句分隔符
```

### 4. 编码问题
**问题表现**：
```powershell
echo "中文内容"
# 显示乱码或编码错误
```

### 5. AI时间戳规范问题 🆕
**问题表现**：
- AI回复缺少时间戳
- 时间戳格式不标准
- 使用历史日期而非实时时间

## ✅ 完美解决方案

### 1. Git配置优化

#### 方案A：全局禁用分页器（推荐）
```powershell
# 设置Git使用cat作为分页器（实际上禁用分页）
git config --global core.pager cat

# 验证配置
git config --global --get core.pager
```

#### 方案B：使用--no-pager参数
```powershell
# 在需要的命令前加 --no-pager
git --no-pager log --oneline -5
git --no-pager show commit_hash
git --no-pager diff
```

#### 方案C：设置环境变量
```powershell
# 在PowerShell配置文件中添加
$env:GIT_PAGER = "cat"
```

### 2. 通配符处理

#### 问题解决
```powershell
# 错误方式
pip install --dry-run dist/*.whl

# 正确方式1：使用Get-ChildItem
$wheelFile = (Get-ChildItem dist/*.whl)[0].FullName
pip install --dry-run $wheelFile

# 正确方式2：使用PowerShell展开
pip install --dry-run (Get-ChildItem dist/*.whl | Select-Object -First 1).FullName

# 正确方式3：在代码中处理
$wheelFiles = Get-ChildItem dist -Filter "*.whl"
if ($wheelFiles) {
    pip install --dry-run $wheelFiles[0].FullName
}
```

### 3. 命令连接

#### PowerShell方式
```powershell
# 错误方式（Bash语法）
git add file.txt && git commit -m "message"

# 正确方式1：使用分号
git add file.txt; git commit -m "message"

# 正确方式2：使用条件执行
git add file.txt
if ($LASTEXITCODE -eq 0) {
    git commit -m "message"
}

# 正确方式3：使用PowerShell操作符
git add file.txt -and (git commit -m "message")
```

### 4. 编码配置

#### UTF-8编码设置
```powershell
# 设置控制台编码
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8

# 设置PowerShell默认编码
$PSDefaultParameterValues['*:Encoding'] = 'utf8'

# 设置Git编码
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8
git config --global i18n.logoutputencoding utf-8
```

### 5. AI配置v2.0和时间戳规范 🆕

#### 时间戳规范要求
```powershell
# 获取标准时间戳
Get-Date -Format "yyyy-MM-dd HH:mm"

# 标准时间戳格式
"[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')]"

# 时间戳辅助函数
function Get-LADTimestamp {
    return "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')]"
}
```

#### AI配置文件v2.0结构
```json
{
    "version": "2.0",
    "project_type": "PowerShell开发环境",
    "ai_behavior_rules": {
        "时间戳规范": {
            "强制要求": "每次回复开头包含[⏰ 时间：YYYY-MM-DD HH:mm]",
            "获取方法": "Get-Date -Format 'yyyy-MM-dd HH:mm'",
            "验证机制": "检查时间戳格式和时效性"
        },
        "命令输出规则": "使用分号(;)作为分隔符",
        "PowerShell集成": "使用PowerShell原生语法"
    }
}
```

## 🔧 自动化配置脚本

### PowerShell配置文件设置

#### 1. 找到配置文件位置
```powershell
# 查看配置文件路径
$PROFILE

# 如果文件不存在，创建它
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}
```

#### 2. 添加优化配置
```powershell
# 编辑配置文件
notepad $PROFILE

# 在文件中添加以下内容：
```

#### 3. 配置文件内容（v1.1增强版）
```powershell
# PowerShell 优化配置 v1.1
# 支持AI配置文件v2.0和时间戳规范
# [⏰ 时间：2025-06-24 11:54]

# 编码设置
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
$PSDefaultParameterValues['*:Encoding'] = 'utf8'

# Git环境变量
$env:GIT_PAGER = "cat"

# LAD项目时间戳辅助函数（符合AI配置v2.0规范）
function Get-LADTimestamp {
    return "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')]"
}

# AI配置文件v2.0验证函数
function Test-AIConfigV2 {
    if (Test-Path ".ai-config.json") {
        try {
            $config = Get-Content ".ai-config.json" | ConvertFrom-Json
            if ($config.version -eq "2.0") {
                Write-Host "$(Get-LADTimestamp) AI配置文件v2.0验证通过" -ForegroundColor Green
                return $true
            }
        } catch {
            Write-Host "$(Get-LADTimestamp) AI配置文件格式错误" -ForegroundColor Red
        }
    }
    Write-Host "$(Get-LADTimestamp) 未发现AI配置文件v2.0" -ForegroundColor Yellow
    return $false
}

# 常用别名
Set-Alias -Name ll -Value Get-ChildItem
Set-Alias -Name grep -Value Select-String

# 函数：安全的Git命令
function git-safe {
    param([string]$Command)
    Write-Host "$(Get-LADTimestamp) 执行Git命令: $Command" -ForegroundColor Cyan
    Invoke-Expression "git --no-pager $Command"
}

# 函数：处理通配符文件
function Get-FirstFile {
    param([string]$Pattern)
    Write-Host "$(Get-LADTimestamp) 查找文件: $Pattern" -ForegroundColor Cyan
    $files = Get-ChildItem $Pattern -ErrorAction SilentlyContinue
    if ($files) {
        Write-Host "$(Get-LADTimestamp) 找到文件: $($files[0].FullName)" -ForegroundColor Green
        return $files[0].FullName
    }
    Write-Host "$(Get-LADTimestamp) 未找到匹配文件" -ForegroundColor Yellow
    return $null
}

# 函数：安全的pip安装（支持时间戳）
function pip-install-wheel {
    param([string]$DistPath = "dist")
    Write-Host "$(Get-LADTimestamp) 开始wheel文件安装..." -ForegroundColor Cyan
    $wheelFile = Get-FirstFile "$DistPath/*.whl"
    if ($wheelFile) {
        Write-Host "$(Get-LADTimestamp) 执行pip安装: $wheelFile" -ForegroundColor Green
        pip install --dry-run $wheelFile
    } else {
        Write-Host "$(Get-LADTimestamp) 在 $DistPath 中未找到wheel文件" -ForegroundColor Red
    }
}

# 函数：时间戳验证
function Test-TimestampFormat {
    param([string]$Timestamp)
    $pattern = '^\[⏰ 时间：\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]'
    if ($Timestamp -match $pattern) {
        Write-Host "$(Get-LADTimestamp) 时间戳格式验证通过" -ForegroundColor Green
        return $true
    } else {
        Write-Host "$(Get-LADTimestamp) 时间戳格式验证失败" -ForegroundColor Red
        return $false
    }
}

Write-Host "$(Get-LADTimestamp) PowerShell 优化配置v1.1已加载" -ForegroundColor Green
Test-AIConfigV2
```

## 🧪 配置验证和测试

### 验证AI配置v2.0
```powershell
# 检查AI配置文件
if (Test-Path ".ai-config.json") {
    $config = Get-Content ".ai-config.json" | ConvertFrom-Json
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] AI配置版本: $($config.version)" -ForegroundColor Green
} else {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] AI配置文件不存在" -ForegroundColor Red
}
```

### 测试时间戳功能
```powershell
# 测试时间戳生成
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 时间戳测试" -ForegroundColor Cyan

# 使用辅助函数
Write-Host "$(Get-LADTimestamp) 使用辅助函数生成时间戳" -ForegroundColor Green

# 验证时间戳格式
$testTimestamp = "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')]"
Test-TimestampFormat $testTimestamp
```

## 📋 使用指南（v1.1版本）

### 立即生效的功能
无需任何操作，以下功能已在所有项目中生效：
- ✅ Git命令不再有分页器问题
- ✅ 不会出现`:...skipping...`和`(END)`提示
- ✅ 不需要按Ctrl+C中断
- ✅ 中文字符正确显示
- ✅ 所有Git操作流畅执行
- ✅ AI配置文件v2.0支持 🆕
- ✅ 时间戳规范自动验证 🆕

### 需要激活的功能
如需使用PowerShell增强功能，请执行：
```powershell
# 方法1：重启PowerShell

# 方法2：重新加载配置
. $PROFILE

# 方法3：运行配置脚本
.\setup-powershell-simple.ps1

# 方法4：测试时间戳功能 🆕
.\setup-windows-dev-env.ps1 -TimestampTest
```

### 验证配置状态
```powershell
# 检查Git配置
git config --global --get core.pager

# 检查PowerShell配置
Test-Path $PROFILE

# 测试自定义函数
Get-FirstFile "*.md"

# 验证AI配置v2.0 🆕
Test-AIConfigV2

# 测试时间戳格式 🆕
Test-TimestampFormat "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')]"
```

## 🔧 故障排除

### 如果某个项目中Git仍有问题

#### 检查本地仓库配置
```powershell
# 在项目目录中执行
git config --local --get core.pager

# 如果有本地配置，删除它
git config --local --unset core.pager
```

#### 强制使用全局配置
```powershell
# 临时解决方案
git --no-pager [command]

# 永久解决方案
git config --global core.pager cat
```

### 如果PowerShell函数不可用

#### 检查配置文件
```powershell
# 检查配置文件是否存在
Test-Path $PROFILE

# 查看配置文件内容
Get-Content $PROFILE

# 重新加载配置
. $PROFILE
```

#### 重新运行配置脚本
```powershell
.\setup-powershell-simple.ps1
```

### AI配置v2.0问题排除 🆕

#### 检查AI配置文件
```powershell
# 验证配置文件存在性
if (!(Test-Path ".ai-config.json")) {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 创建AI配置文件..." -ForegroundColor Yellow
    .\setup-windows-dev-env.ps1 -SkipPowerShell -SkipGit -SkipEditor
}

# 验证配置文件格式
try {
    $config = Get-Content ".ai-config.json" | ConvertFrom-Json
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] AI配置文件格式正确" -ForegroundColor Green
} catch {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] AI配置文件格式错误，重新生成..." -ForegroundColor Red
    .\setup-windows-dev-env.ps1 -Force -SkipPowerShell -SkipGit -SkipEditor
}
```

#### 时间戳问题排除
```powershell
# 检查时间戳函数
if (Get-Command Get-LADTimestamp -ErrorAction SilentlyContinue) {
    Write-Host "$(Get-LADTimestamp) 时间戳函数可用" -ForegroundColor Green
} else {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 时间戳函数不可用，重新加载配置..." -ForegroundColor Yellow
    . $PROFILE
}

# 验证时间戳格式
$testTimestamp = "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')]"
if (Test-TimestampFormat $testTimestamp) {
    Write-Host "$(Get-LADTimestamp) 时间戳格式验证通过" -ForegroundColor Green
} else {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 时间戳格式验证失败" -ForegroundColor Red
}
```

## 📈 配置优势

### 系统级别的稳定性
- **一次配置，全局生效**：不需要在每个项目中重复配置
- **跨项目一致性**：所有项目使用相同的Git行为
- **持久化配置**：系统重启后仍然有效
- **AI配置标准化**：统一的AI行为规则和时间戳规范 🆕

### 开发效率提升
- **无中断操作**：Git命令流畅执行，不被分页器打断
- **统一体验**：在所有项目中都有相同的命令行体验
- **智能时间戳**：自动生成和验证时间戳格式 🆕
- **AI配置集成**：完整的AI工作流程支持 🆕

### v1.1版本新特性 🆕
- **AI配置文件v2.0支持**：完整的AI行为规则配置
- **时间戳规范自动化**：标准化的时间戳生成和验证
- **增强的函数库**：更多实用的PowerShell辅助函数
- **配置验证机制**：自动检查和修复配置问题
- **跨项目兼容性**：支持LAD项目生态系统

## 📚 相关文档

- [Windows开发环境一键配置指南.md](Windows开发环境一键配置指南.md)
- [PowerShell配置作用范围说明.md](PowerShell配置作用范围说明.md)
- [AI-Prompts-Templates/](AI-Prompts-Templates/) - AI配置提示词模板库
- [.ai-config.json](.ai-config.json) - AI配置文件v2.0

---

**最后更新**: 2025-06-24 11:54  
**版本**: v1.1  
**支持**: AI配置文件v2.0 + 时间戳规范