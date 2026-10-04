# AUTO-START CHATBOT SERVER ON WINDOWS STARTUP

## Quick Method: Add to Windows Startup Folder

1. **Open Startup Folder:**
   - Press `Win + R`
   - Type: `shell:startup`
   - Press Enter

2. **Create Shortcut to START_SERVER.bat:**
   - Right-click in the startup folder
   - Select "New" → "Shortcut"
   - Paste this path:
     ```
     C:\Users\sakshi\OneDrive\Desktop\chatbot\START_SERVER.bat
     ```
   - Click Next → Finish

3. **Restart your laptop** → Server starts automatically! ✅

---

## Advanced Method: Task Scheduler (Runs hidden in background)

1. **Press `Win + R` → Type `taskschd.msc` → Enter**

2. **Create New Task:**
   - Right-click "Task Scheduler Library" → "Create Basic Task..."
   - Name: `Sentinel Alpha - Auto Start`
   - Description: `Automatically start emergency chatbot server`
   - Click Next

3. **Trigger:**
   - Select "At startup"
   - Click Next

4. **Action:**
   - Select "Start a program"
   - Program: `python.exe`
   - Arguments: `ai_service.py`
   - Start in: `C:\Users\sakshi\OneDrive\Desktop\chatbot`
   - Click Next → Finish

5. **Right-click the task → Properties:**
   - Uncheck "Stop if running longer than..."
   - Click OK

---

## Important Notes:

⚠️ **Keep Running:**
- If you use Method 1, a terminal window will stay open
- This is **normal** - the server needs to keep running
- Do NOT close the terminal window or the server stops!

---

## Testing It:

1. Restart your laptop
2. After 10-15 seconds, open browser
3. Go to `http://localhost:5000` or open your chatbot
4. Should be ONLINE ✅ (not offline)

---

## Troubleshooting:

**Still showing offline?**
1. Check if Python server started: Open `http://localhost:5000` in browser
2. If blank/error, terminal crashed - start manually instead
3. Check Python is installed: Open PowerShell, type `python --version`

**Server closes when you restart?**
- Use Task Scheduler method (runs in background)
- Or keep the START_SERVER.bat terminal window open
