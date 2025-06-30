# PowerShell 问题修复脚本
# 解决Git分页器和编码问题

Write-Host "=== PowerShell 环境修复 ===" -ForegroundColor Cyan

# 1. 修复Git分页器问题
Write-Host "修复Git分页器问题..." -ForegroundColor Yellow
git config --global core.pager cat
Write-Host "✅ Git分页器已设置为cat" -ForegroundColor Green

# 2. 修复Git编码问题
Write-Host "修复Git编码问题..." -ForegroundColor Yellow
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8
git config --global i18n.logoutputencoding utf-8
Write-Host "✅ Git编码已设置为UTF-8" -ForegroundColor Green

# 3. 验证修复结果
Write-Host "验证修复结果..." -ForegroundColor Yellow
$pager = git config --global --get core.pager
$quotepath = git config --global --get core.quotepath

if ($pager -eq "cat") {
    Write-Host "✅ Git分页器配置正确: $pager" -ForegroundColor Green
} else {
    Write-Host "❌ Git分页器配置异常: $pager" -ForegroundColor Red
}

if ($quotepath -eq "false") {
    Write-Host "✅ Git编码配置正确" -ForegroundColor Green
} else {
    Write-Host "❌ Git编码配置异常" -ForegroundColor Red
}

Write-Host "`n🎉 修复完成！现在可以正常使用Git命令了" -ForegroundColor Green
Write-Host "💡 Git命令不会再出现分页器问题" -ForegroundColor Cyan

# 4. 测试Git命令
Write-Host "`n测试Git命令..." -ForegroundColor Yellow
git log --oneline -3
Write-Host "✅ Git命令测试完成" -ForegroundColor Green 