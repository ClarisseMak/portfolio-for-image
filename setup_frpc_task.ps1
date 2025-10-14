# 创建 FRP 客户端自动启动任务
# 需要以管理员身份运行 PowerShell

$action = New-ScheduledTaskAction `
    -Execute "D:\frp_0.65.0_windows_amd64\frp_0.65.0_windows_amd64\frpc.exe" `
    -Argument "-c frpc.toml" `
    -WorkingDirectory "D:\frp_0.65.0_windows_amd64\frp_0.65.0_windows_amd64"

$trigger = New-ScheduledTaskTrigger -AtLogOn

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Days 0)

$principal = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType Interactive -RunLevel Highest

Register-ScheduledTask `
    -TaskName "FRP Client Auto Start" `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal `
    -Description "开机自动启动 FRP 客户端" `
    -Force

Write-Host "✓ 任务计划已创建成功！" -ForegroundColor Green
Write-Host "任务名称: FRP Client Auto Start" -ForegroundColor Cyan
Write-Host "可以在'任务计划程序'中查看和管理" -ForegroundColor Yellow

