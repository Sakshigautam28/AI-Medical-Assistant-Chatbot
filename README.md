# 🆘 Sentinel Alpha - Emergency AI Chatbot

A real-time emergency response chatbot with AI-powered guidance and admin tracking dashboard.

---

## 📋 Project Structure

```
chatbot/
├── ai_service.py              # Flask backend (MAIN ENGINE)
├── index.html                 # Full chatbot interface
├── chatbot_widget.html        # Floating widget (embed anywhere)
├── admin_dashboard.html       # Admin tracking dashboard
├── admin_dashboard.html       # (Legacy) Admin panel
└── README.md                  # This file
```

---

## 🚀 Quick Start for Your Teammate

### **STEP 1: Setup Backend**

1. **Extract the chatbot folder** from zip
2. **Install Python** (3.10+) from python.org if not installed
3. **Install dependencies**:
   ```bash
   pip install flask flask-cors google-genai
   ```

4. **Get your Google Gemini API Key**:
   - Go to: https://makersuite.google.com/app/apikey
   - Copy your API key
   - Update line 7 in `ai_service.py`:
     ```python
     GEMINI_API_KEY = "YOUR_API_KEY_HERE"
     ```

5. **Start the backend** (from command line/terminal):
   ```bash
   python ai_service.py
   ```
   You should see:
   ```
   * Running on http://127.0.0.1:5000
   * Running on http://10.2.8.241:5000
   ```

---

### **STEP 2: Use the Chatbot**

#### **Option A: Full Chatbot Interface**
Open `index.html` in your browser:
- Complete chat experience
- Voice input/output
- Live map with GPS
- Emergency SOS button

#### **Option B: Floating Widget** (EMBED IN YOUR WEBSITE)
This is the **easiest way to integrate into another website**:

**In your website's HTML**, add this ONE line at the end of `<body>`:
```html
<iframe src="http://localhost:5000/../chatbot_widget.html" 
        style="position: fixed; bottom: 20px; right: 20px; border: none; z-index: 9999;"></iframe>
```

OR use this script approach (NO iframe needed):
```html
<script>
    window.sentinelConfig = {
        backendUrl: "http://localhost:5000"  // Your backend URL
    };
</script>
<script src="http://localhost:5000/../chatbot_widget.html"></script>
```

The widget will appear as a **floating red button** in the bottom-right corner! 🎯

---

### **STEP 3: Admin Tracking**

Open `admin_dashboard.html` to:
- 📍 View all victim locations on a live map
- 📊 Check real-time statistics
- ✅ Update victim status (Assign, In Progress, Resolved)
- 🔄 Auto-refreshes every 5 seconds

---

## 🔗 API Endpoints (For Developers)

### **Chatbot Endpoint**
```
POST /chatbot
Headers: Content-Type: application/json

Body:
{
    "user_id": "unique_user_id",
    "symptoms": "describe the problem",
    "disaster": "medical|flood|earthquake|fire",
    "lat": 20.5,
    "lng": 78.9
}

Response:
{
    "advice": ["First, stay calm..."]
}
```

### **Emergency SOS Endpoint**
```
POST /dispatch_volunteer
Body:
{
    "symptoms": "MANUAL SOS TRIGGERED",
    "disaster": "medical",
    "lat": 20.5,
    "lng": 78.9
}

Response:
{
    "status": "success",
    "victim_id": 1
}
```

### **Admin Endpoints**
```
GET /admin/victims
Response:
{
    "total_victims": 5,
    "victims": [
        {
            "id": 1,
            "symptoms": "...",
            "lat": 20.5,
            "lng": 78.9,
            "disaster": "medical",
            "status": "UNASSIGNED",
            "timestamp": "2026-04-12 06:35:11"
        }
    ]
}

POST /admin/update_victim
Body: {"victim_id": 1, "status": "ASSIGNED"}
```

---

## 🌐 Network Setup

### **Share Across Network**
If you want to access from another PC on the same WiFi:

1. **Find your IP address**:
   ```bash
   # Windows
   ipconfig
   # Look for IPv4 Address (e.g., 192.168.x.x or 10.x.x.x)
   ```

2. **Teammate accesses via**:
   ```
   http://YOUR_IP:5000
   ```

3. **Share these URLs**:
   - Chatbot: `http://YOUR_IP:5000/index.html`
   - Widget: `http://YOUR_IP:5000/chatbot_widget.html`
   - Admin: `http://YOUR_IP:5000/admin_dashboard.html`

---

## 📦 How to Share the Project

### **Method 1: ZIP File (Easiest)**
```bash
# Windows: Right-click folder → Send to → Compressed folder
# Mac/Linux: zip -r chatbot.zip chatbot/
```
Send `chatbot.zip` to your teammate ✉️

### **Method 2: GitHub (For Teams)**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_GITHUB_REPO
git push -u origin main
```
Share GitHub link with teammate

### **Method 3: Google Drive/OneDrive**
Just upload the folder and share link

---

## ⚙️ Configuration

### **Backend Port** (in `ai_service.py`)
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to another port if needed
```

### **Widget Backend URL** (in `chatbot_widget.html`)
The widget automatically detects:
- **Local**: `http://localhost:5000`
- **Network**: `http://10.2.8.241:5000`

Or hardcode by adding before the widget:
```html
<script>
    window.sentinelConfig = {
        backendUrl: "http://YOUR_BACKEND_URL:5000"
    };
</script>
```

---

## 🐛 Troubleshooting

### **"Backend not connected"**
- ✅ Make sure `python ai_service.py` is running
- ✅ Check backend URL matches your IP
- ✅ Check firewall isn't blocking port 5000

### **"API key is invalid"**
- ✅ Get new key from: https://makersuite.google.com/app/apikey
- ✅ Update `GEMINI_API_KEY` in `ai_service.py`
- ✅ Restart `python ai_service.py`

### **"Model not found"**
- ✅ Already fixed - uses `gemini-2.5-flash`
- ✅ Ensure your API key has access to this model

### **Widget not showing on my website**
- ✅ Change `http://localhost:5000` to your actual backend URL
- ✅ Check browser console for CORS errors
- ✅ Ensure backend has `CORS(app)` enabled (it does ✓)

---

## 🎯 Features

✅ **Real-time AI Chat** - Powered by Google Gemini  
✅ **Voice I/O** - Speak and listen to responses  
✅ **Location Tracking** - GPS integration  
✅ **Emergency SOS** - One-click dispatch  
✅ **Admin Dashboard** - Real-time victim tracking  
✅ **Floating Widget** - Embed anywhere  
✅ **Multi-user Support** - Handles multiple users simultaneously  
✅ **Status Management** - Track victim progress  

---

## 📞 Support

For issues:
1. Check error messages in Python terminal
2. Check browser console (F12)
3. Restart backend: `python ai_service.py`
4. Clear browser cache (Ctrl+Shift+Del)

---

## 📄 License

Private Project - Use as needed!

---

**Happy emergency response! 🚀**
