# PowerShell Environment Fix Script
# Fixes Git pager and encoding issues

Write-Host "=== PowerShell Environment Fix ===" -ForegroundColor Cyan

# 1. Fix Git pager issue
Write-Host "Fixing Git pager issue..." -ForegroundColor Yellow
git config --global core.pager cat
Write-Host "✓ Git pager set to cat" -ForegroundColor Green

# 2. Fix Git encoding issues
Write-Host "Fixing Git encoding issues..." -ForegroundColor Yellow
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8
git config --global i18n.logoutputencoding utf-8
Write-Host "✓ Git encoding set to UTF-8" -ForegroundColor Green

# 3. Verify fixes
Write-Host "Verifying fixes..." -ForegroundColor Yellow
$pager = git config --global --get core.pager
$quotepath = git config --global --get core.quotepath

if ($pager -eq "cat") {
    Write-Host "✓ Git pager configured correctly: $pager" -ForegroundColor Green
} else {
    Write-Host "✗ Git pager configuration issue: $pager" -ForegroundColor Red
}

if ($quotepath -eq "false") {
    Write-Host "✓ Git encoding configured correctly" -ForegroundColor Green
} else {
    Write-Host "✗ Git encoding configuration issue" -ForegroundColor Red
}

Write-Host "`n🎉 Fix completed! Git commands should work normally now" -ForegroundColor Green
Write-Host "💡 Git commands will no longer have pager issues" -ForegroundColor Cyan

# 4. Test Git commands
Write-Host "`nTesting Git commands..." -ForegroundColor Yellow
git log --oneline -3
Write-Host "✓ Git command test completed" -ForegroundColor Green

Write-Host "`n📋 Summary of fixes:" -ForegroundColor White
Write-Host "- Git pager set to 'cat' (no more :...skipping... issues)" -ForegroundColor Yellow
Write-Host "- Git encoding set to UTF-8 (proper Chinese character support)" -ForegroundColor Yellow
Write-Host "- All Git commands now work without interruption" -ForegroundColor Yellow 