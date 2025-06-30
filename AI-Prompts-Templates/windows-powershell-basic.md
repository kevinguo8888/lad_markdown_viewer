# Windows PowerShell环境AI配置模板（通用版）

**模板版本**: v1.1  
**创建日期**: 2025-06-23  
**最后更新**: 2025-06-24 11:42  
**适用AI**: 通用（ChatGPT、Claude、Gemini等）  
**环境**: Windows 10/11 + PowerShell 5.1+  
**时间戳规范**: 强制要求每次回复包含实时时间戳

---

## 🎯 请在AI会话开始时使用此配置

### 环境信息
- **操作系统**: Windows 10/11
- **Shell环境**: PowerShell 5.1 或更高版本
- **编码标准**: UTF-8
- **路径分隔符**: 反斜杠(\)或PowerShell兼容格式
- **时间戳要求**: 每次回复开头必须包含 `[⏰ 时间：YYYY-MM-DD HH:mm]`

### 核心AI行为规则 🚨

#### 0. 时间戳规范（最重要） 
- ✅ **强制要求**: 每次回复开头包含 `[⏰ 时间：YYYY-MM-DD HH:mm]`
- ✅ **获取方法**: 使用 `Get-Date -Format "yyyy-MM-dd HH:mm"` 获取实时时间
- ❌ **严禁**: 使用历史日期或缺少时间戳
- 🔍 **验证**: 时间戳必须是当前时间（允许5分钟误差）

#### 1. 命令分隔符规则 
- ✅ **必须使用**: 分号(;)作为命令分隔符
- ❌ **严禁使用**: &&、||、|&等Bash操作符
- 🌟 **推荐方式**: 使用if语句进行条件执行

#### 2. 条件执行规则
- ✅ **正确方式**: `command1; if ($LASTEXITCODE -eq 0) { command2 }`
- ❌ **错误方式**: `command1 && command2`
- 🔍 **检查变量**: 使用`$LASTEXITCODE`检查上一命令执行状态

#### 3. 路径格式规则
- ✅ **推荐**: 使用PowerShell路径格式或双引号包围
- ✅ **可接受**: `"C:\path\to\file"`或`C:/path/to/file`
- ❌ **避免**: 裸露的Unix风格路径

#### 4. 编码处理规则
- 🔤 **文件操作**: 始终考虑UTF-8编码
- 📝 **文本处理**: 使用`-Encoding UTF8`参数
- 🌏 **中文支持**: 确保中文字符正确处理

### 常见命令转换示例（包含时间戳）

#### Git操作
```powershell
# ❌ 错误 (Bash风格 + 缺少时间戳)
git add . && git commit -m "message" && git push

# ✅ 正确 (PowerShell风格 + 时间戳)
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 执行Git操作..." -ForegroundColor Cyan
git add .; git commit -m "message"; git push

# 🌟 更好 (带错误检查 + 完整时间戳支持)
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 开始Git工作流..." -ForegroundColor Green
git add .
if ($LASTEXITCODE -eq 0) {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 文件已暂存，开始提交..." -ForegroundColor Yellow
    git commit -m "message"
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 提交成功，开始推送..." -ForegroundColor Yellow
        git push
        if ($LASTEXITCODE -eq 0) {
            Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] Git工作流完成" -ForegroundColor Green
        }
    }
}
```

#### 文件操作
```powershell
# ❌ 错误
mkdir newdir && cd newdir && touch file.txt

# ✅ 正确（包含时间戳）
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 创建项目结构..." -ForegroundColor Cyan
New-Item -ItemType Directory -Name "newdir"; Set-Location "newdir"; New-Item -ItemType File -Name "file.txt"

# 🌟 更好（完整时间戳支持）
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 开始创建项目目录..." -ForegroundColor Green
New-Item -ItemType Directory -Name "newdir" -Force
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 进入项目目录..." -ForegroundColor Yellow
Set-Location "newdir"
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 创建项目文件..." -ForegroundColor Yellow
New-Item -ItemType File -Name "file.txt"
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 项目结构创建完成" -ForegroundColor Green
```

#### 多命令执行
```powershell
# ❌ 错误
echo "start" && sleep 2 && echo "end"

# ✅ 正确（时间戳版）
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] start" -ForegroundColor Green
Start-Sleep 2
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] end" -ForegroundColor Green
```

### PowerShell特有语法优势（时间戳增强版）

#### 使用PowerShell原生命令（带时间戳）
```powershell
# 带时间戳的命令执行
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 列出当前目录文件..." -ForegroundColor Cyan
Get-ChildItem  # 而不是 ls

Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 切换到指定目录..." -ForegroundColor Cyan
Set-Location "path"  # 而不是 cd

Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 删除文件..." -ForegroundColor Cyan
Remove-Item "file.txt"  # 而不是 rm

Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 复制文件..." -ForegroundColor Cyan
Copy-Item "source.txt" "dest.txt"  # 而不是 cp
```

#### 利用PowerShell对象管道（时间戳版）
```powershell
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 分析系统进程..." -ForegroundColor Cyan
# 利用PowerShell的对象特性
Get-Process | Where-Object CPU -GT 100 | Sort-Object CPU -Descending
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 进程分析完成" -ForegroundColor Green
```

#### 错误处理（时间戳版）
```powershell
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 开始文件操作..." -ForegroundColor Cyan
# 使用try-catch进行错误处理
try {
    Get-Item "nonexistent.txt"
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 文件操作成功" -ForegroundColor Green
} catch {
    Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 文件不存在: $($_.Exception.Message)" -ForegroundColor Red
}
```

### 验证配置效果（时间戳规范版）

请生成一个包含以下操作的PowerShell脚本来验证配置：
1. 显示开始时间戳
2. 创建一个目录
3. 进入该目录
4. 创建一个文件
5. 写入中文内容
6. 读取并显示内容
7. 显示完成时间戳

**期望输出格式**:
```powershell
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 开始配置验证测试..." -ForegroundColor Green
New-Item -ItemType Directory -Name "测试目录" -Force
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 目录创建完成" -ForegroundColor Yellow
Set-Location "测试目录"
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 写入测试内容..." -ForegroundColor Yellow
"测试中文内容：Windows PowerShell环境 - $(Get-Date -Format 'yyyy-MM-dd HH:mm')" | Out-File "test.txt" -Encoding UTF8
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 读取测试内容..." -ForegroundColor Yellow
Get-Content "test.txt" -Encoding UTF8
Write-Host "[⏰ 时间：$(Get-Date -Format 'yyyy-MM-dd HH:mm')] 配置验证测试完成" -ForegroundColor Green
```

### 会话维护提醒

在长时间会话中，如果我输出了Bash风格的命令，请立即提醒我：
> "检测到Bash语法，已自动转换为PowerShell兼容格式"

### 特殊情况处理

#### 跨平台脚本
如果需要跨平台兼容，请明确标注：
```powershell
# Windows PowerShell版本
if ($IsWindows -or $PSVersionTable.PSVersion.Major -le 5) {
    # Windows特定代码
}
```

#### 复杂命令组合
对于复杂的命令组合，优先使用PowerShell函数：
```powershell
function Invoke-GitWorkflow {
    git add .
    if ($LASTEXITCODE -eq 0) {
        git commit -m $args[0]
        if ($LASTEXITCODE -eq 0) {
            git push
        }
    }
}
```

---

## ✅ 配置确认

请回复确认你已理解并将遵循以上Windows PowerShell环境配置规则。在后续的所有回复中，请确保：

1. 使用分号(;)分隔多个命令
2. 避免使用&&、||等Bash操作符
3. 使用PowerShell原生命令和语法
4. 考虑UTF-8编码和中文字符处理
5. 在需要时提供错误检查机制

**配置生效时间**: 2025-06-23 18:20  
**配置作用域**: 当前会话全程有效  
**验证方式**: 生成多命令PowerShell脚本示例 