@echo off
cd /d D:\frp_0.65.0_windows_amd64\frp_0.65.0_windows_amd64
start /min frpc.exe -c frpc.toml

REM 说明：
REM @echo off - 不显示命令本身
REM cd /d - 切换到指定目录（/d 允许跨盘符）
REM start /min - 最小化窗口启动
REM 如果要隐藏窗口，可以使用 VBScript 包装器

