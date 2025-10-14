# 删除 FRP 客户端自动启动任务
# 需要以管理员身份运行 PowerShell

try {
    Unregister-ScheduledTask -TaskName "FRP Client Auto Start" -Confirm:$false
    Write-Host "✓ 任务计划已删除成功！" -ForegroundColor Green
} catch {
    Write-Host "✗ 删除失败: $_" -ForegroundColor Red
}

