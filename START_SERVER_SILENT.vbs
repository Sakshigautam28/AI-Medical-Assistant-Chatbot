Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Get the current script's directory
scriptPath = objFSO.GetParentFolderName(WScript.ScriptFullName)

' Change to chatbot directory
objShell.CurrentDirectory = scriptPath

' Start Python server silently (no terminal window)
objShell.Run "python ai_service.py", 0, False

' Wait a moment to ensure server started
WScript.Sleep 2000

' Optional: Open browser
' objShell.Run "http://localhost:5000"
