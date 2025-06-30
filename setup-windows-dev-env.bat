@echo off
chcp 65001 >nul
REM Windows开发环境一键配置脚本 (批处理版本) v1.1
REM 适用于通用Windows开发环境配置
REM 支持AI配置文件v2.0和时间戳规范
REM [⏰ 时间：2025-06-24 11:54]

echo.

REM 显示当前时间戳（符合AI行为规则）
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do set mydate=%%c-%%a-%%b
for /f "tokens=1-2 delims=: " %%a in ('time /t') do set mytime=%%a:%%b
echo [⏰ 时间：%mydate% %mytime%] 开始Windows开发环境配置...

echo.
echo ============================================================
echo 🚀 Windows开发环境一键配置 (批处理版本) v1.1
echo ============================================================
echo 配置类型: 通用Windows开发环境
echo 支持功能: AI配置文件v2.0 + 时间戳规范
echo 配置时间: %date% %time%
echo.

REM 检查PowerShell是否可用
powershell -Command "Write-Host '[⏰ 时间：$(Get-Date -Format \"yyyy-MM-dd HH:mm\")] 检查PowerShell环境...' -ForegroundColor Green"
if %errorlevel% neq 0 (
    echo [⏰ 时间：%mydate% %mytime%] ❌ PowerShell不可用，请确保PowerShell已安装
    pause
    exit /b 1
)

REM 检查脚本文件是否存在
if not exist "setup-windows-dev-env.ps1" (
    echo [⏰ 时间：%mydate% %mytime%] ❌ 找不到PowerShell配置脚本: setup-windows-dev-env.ps1
    echo 请确保脚本文件在当前目录中
    pause
    exit /b 1
)

echo 📋 配置选项 (v1.1增强版):
echo 1. 完整配置 (推荐) - 包含AI配置v2.0
echo 2. 仅配置PowerShell编码 + 时间戳支持
echo 3. 仅配置Git环境
echo 4. 仅配置AI工具 + 时间戳规范
echo 5. 仅配置代码编辑器
echo 6. 配置并验证 (包含AI配置验证)
echo 7. 强制覆盖现有配置
echo 8. 自定义配置
echo 9. 验证AI配置文件v2.0
echo.

set /p choice="请选择配置选项 (1-9): "

if "%choice%"=="1" (
    echo [⏰ 时间：%mydate% %mytime%] 🚀 执行完整配置（包含AI配置v2.0）...
    powershell -ExecutionPolicy Bypass -File "setup-windows-dev-env.ps1"
) else if "%choice%"=="2" (
    echo [⏰ 时间：%mydate% %mytime%] 🔧 仅配置PowerShell编码 + 时间戳支持...
    powershell -ExecutionPolicy Bypass -File "setup-windows-dev-env.ps1" -SkipGit -SkipAI -SkipEditor
) else if "%choice%"=="3" (
    echo [⏰ 时间：%mydate% %mytime%] 📁 仅配置Git环境...
    powershell -ExecutionPolicy Bypass -File "setup-windows-dev-env.ps1" -SkipPowerShell -SkipAI -SkipEditor
) else if "%choice%"=="4" (
    echo [⏰ 时间：%mydate% %mytime%] 🤖 仅配置AI工具 + 时间戳规范...
    powershell -ExecutionPolicy Bypass -File "setup-windows-dev-env.ps1" -SkipPowerShell -SkipGit -SkipEditor
) else if "%choice%"=="5" (
    echo [⏰ 时间：%mydate% %mytime%] 🎯 仅配置代码编辑器...
    powershell -ExecutionPolicy Bypass -File "setup-windows-dev-env.ps1" -SkipPowerShell -SkipGit -SkipAI
) else if "%choice%"=="6" (
    echo [⏰ 时间：%mydate% %mytime%] 🔍 配置并验证（包含AI配置验证）...
    powershell -ExecutionPolicy Bypass -File "setup-windows-dev-env.ps1" -Verify
) else if "%choice%"=="7" (
    echo [⏰ 时间：%mydate% %mytime%] ⚡ 强制覆盖现有配置...
    powershell -ExecutionPolicy Bypass -File "setup-windows-dev-env.ps1" -Force -Verify
) else if "%choice%"=="8" (
    echo [⏰ 时间：%mydate% %mytime%] 🛠️ 自定义配置选项...
    echo.
    echo 可用参数 (v1.1版本):
    echo   -SkipPowerShell  : 跳过PowerShell编码配置
    echo   -SkipGit         : 跳过Git环境配置
    echo   -SkipAI          : 跳过AI工具配置
    echo   -SkipEditor      : 跳过代码编辑器配置
    echo   -Verify          : 执行配置验证（包含AI配置验证）
    echo   -Force           : 强制覆盖现有配置
    echo   -TimestampTest   : 测试时间戳功能
    echo.
    set /p customParams="请输入自定义参数: "
    powershell -ExecutionPolicy Bypass -File "setup-windows-dev-env.ps1" %customParams%
) else if "%choice%"=="9" (
    echo [⏰ 时间：%mydate% %mytime%] 🔍 验证AI配置文件v2.0...
    powershell -ExecutionPolicy Bypass -Command "if (Test-Path '.ai-config.json') { try { $config = Get-Content '.ai-config.json' | ConvertFrom-Json; Write-Host '[⏰ 时间：$(Get-Date -Format \"yyyy-MM-dd HH:mm\")] AI配置文件版本:' $config.version -ForegroundColor Green; if ($config.version -eq '2.0') { Write-Host '[⏰ 时间：$(Get-Date -Format \"yyyy-MM-dd HH:mm\")] ✅ AI配置v2.0验证通过' -ForegroundColor Green } else { Write-Host '[⏰ 时间：$(Get-Date -Format \"yyyy-MM-dd HH:mm\")] ❌ AI配置版本不是v2.0' -ForegroundColor Red } } catch { Write-Host '[⏰ 时间：$(Get-Date -Format \"yyyy-MM-dd HH:mm\")] ❌ AI配置文件格式错误' -ForegroundColor Red } } else { Write-Host '[⏰ 时间：$(Get-Date -Format \"yyyy-MM-dd HH:mm\")] ❌ AI配置文件不存在' -ForegroundColor Red }"
    goto end
) else (
    echo [⏰ 时间：%mydate% %mytime%] ❌ 无效选项，执行默认完整配置...
    powershell -ExecutionPolicy Bypass -File "setup-windows-dev-env.ps1"
)

echo.
if %errorlevel% equ 0 (
    echo [⏰ 时间：%mydate% %mytime%] ✅ 配置脚本执行完成
) else (
    echo [⏰ 时间：%mydate% %mytime%] ❌ 配置脚本执行失败，错误代码: %errorlevel%
)

:end
echo.
echo 📚 后续步骤 (v1.1版本):
echo 1. 重启PowerShell或运行: powershell -Command ". $PROFILE"
echo 2. 查看配置文档: Windows开发环境一键配置指南.md
echo 3. 使用AI提示词: AI-Prompts-Templates目录
echo 4. 测试时间戳: powershell -Command "Write-Host '[⏰ 时间：$(Get-Date -Format \"yyyy-MM-dd HH:mm\")] 测试'"
echo 5. 验证AI配置: 运行选项9或查看.ai-config.json
echo.
echo 💡 v1.1新特性:
echo - 支持AI配置文件v2.0时间戳规范
echo - 增强的配置验证功能
echo - 完整的时间戳显示支持
echo - AI配置文件独立验证选项
echo.

pause 