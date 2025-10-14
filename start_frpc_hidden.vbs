Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c cd /d D:\frp_0.65.0_windows_amd64\frp_0.65.0_windows_amd64 && frpc.exe -c frpc.toml", 0, False
Set WshShell = Nothing

' 说明：
' 第二个参数 0 表示隐藏窗口
' False 表示不等待程序结束

