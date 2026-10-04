# 📧 SETUP INSTRUCTIONS FOR YOUR TEAMMATE

---

## 📦 What to Share

**ZIP this entire folder and send to your teammate:**
- `chatbot/` folder (all files inside)

**OR use GitHub:**
- Create a repo and share the link

---

## 🚀 Your Teammate Should Do This:

### **Step 1: Extract & Navigate**
```bash
# Windows
Extract the zip file
cd Desktop/chatbot

# Mac/Linux  
unzip chatbot.zip
cd chatbot
```

### **Step 2: Install Virtual Environment** (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Get Google Gemini API Key**
1. Go to: **https://makersuite.google.com/app/apikey**
2. Create new API key (free)
3. Copy the key

### **Step 5: Add API Key to Code**
Open `ai_service.py` (line 7-8):
```python
GEMINI_API_KEY = "PASTE_YOUR_KEY_HERE"
```

### **Step 6: Start Backend**
```bash
python ai_service.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Running on http://10.2.8.241:5000
```

✅ **Backend is running!**

---

## 🎮 How to Use

### **Full Chatbot Interface**
Open in browser: `index.html`
- Chat with AI
- Voice input/output  
- Emergency SOS button
- Live map with location

### **Floating Widget** (Best for embedding)
Open in browser: `chatbot_widget.html`
- Floating red button (bottom-right)
- Click to open chat
- Embed on any website

### **Admin Dashboard**
Open in browser: `admin_dashboard.html`
- See all victim locations on map
- Track victim status
- Update cases (Assign, In Progress, Resolve)

---

## 🌐 EMBEDDING THE WIDGET ON A WEBSITE

This is the **main feature** for your frontend developer!

### **Super Simple Method:**

In their website HTML (before closing `</body>`):
```html
<script>
    window.sentinelConfig = {
        backendUrl: "http://localhost:5000"
    };
</script>

<iframe src="http://localhost:5000/chatbot_widget.html"
        style="position: fixed; bottom: 20px; right: 20px; width: 0; height: 0; border: none; z-index: 9999;"
        allow="geolocation"></iframe>
```

**And BOOM!** 💥 The red emergency button appears in the bottom-right corner!

**See `WIDGET_INTEGRATION.md` for more customization options.**

---

## 📂 Project Files Explained

| File | Purpose |
|------|---------|
| `ai_service.py` | Backend server (THE MOST IMPORTANT) |
| `index.html` | Full chatbot interface |
| `chatbot_widget.html` | 🎯 Floating widget (embed anywhere) |
| `admin_dashboard.html` | Admin victim tracking |
| `requirements.txt` | Python dependencies |
| `README.md` | Complete documentation |
| `WIDGET_INTEGRATION.md` | Widget embedding guide |

---

## 🔗 Key URLs (After Backend Starts)

- **Full App**: http://localhost:5000/index.html
- **Widget**: http://localhost:5000/chatbot_widget.html
- **Admin**: http://localhost:5000/admin_dashboard.html
- **API Docs**: See README.md

---

## ⚙️ Network Setup (For Multiple PCs)

If backend and frontend are on **different computers**:

### **Find Backend IP Address:**
```bash
# Windows - Open Command Prompt
ipconfig

# Look for IPv4 Address (e.g., 192.168.1.100 or 10.0.0.5)
```

### **Use This IP on Frontend:**
```html
<script>
    window.sentinelConfig = {
        backendUrl: "http://192.168.1.100:5000"  // Your backend PC's IP
    };
</script>

<iframe src="http://192.168.1.100:5000/chatbot_widget.html" ...></iframe>
```

---

## 🐛 Troubleshooting

### **"Backend not connected" Error**
✅ Check: `python ai_service.py` is running  
✅ Check: Backend URL is correct (localhost vs IP)  
✅ Check: No firewall blocking port 5000

### **"Model not found" or "API key invalid"**
✅ Get new key: https://makersuite.google.com/app/apikey  
✅ Update `GEMINI_API_KEY` in `ai_service.py`  
✅ Restart backend: `python ai_service.py`

### **Widget not showing on website**
✅ Check URL is correct (http://localhost:5000 or your IP)
✅ Check browser console (F12) for errors
✅ Make sure backend is running

### **CORS errors in console**
Usually not an issue - backend has CORS enabled by default.

---

## 📝 File Checklist

Make sure these files are in the chatbot folder:
- ✅ `ai_service.py` 
- ✅ `index.html`
- ✅ `chatbot_widget.html`
- ✅ `admin_dashboard.html`
- ✅ `requirements.txt`
- ✅ `README.md`
- ✅ `WIDGET_INTEGRATION.md`

---

## 🎯 Summary For Your Teammate

1. **Extract zip** → Navigate to folder
2. **Run**: `pip install -r requirements.txt`
3. **Add API Key** to `ai_service.py`
4. **Run**: `python ai_service.py`
5. **Test**: Open `index.html` or `chatbot_widget.html`
6. **Embed**: Use the widget code in their website HTML

**That's it! Everything else is included.** 🚀

---

## 📞 Questions?

**Ask your teammate to check:**
1. Python terminal for error messages
2. Browser console (F12) for errors
3. README.md for detailed documentation
4. WIDGET_INTEGRATION.md for embedding help

---

**Good luck with your project! 🎊**
