Set oShell = CreateObject("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c notify.bat"
oShell.Run strArgs, 0, false
