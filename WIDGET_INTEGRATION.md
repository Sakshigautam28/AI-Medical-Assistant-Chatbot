# 🎯 Embedding Sentinel Alpha Widget on Your Website

This guide shows how to add the Sentinel Alpha emergency chatbot as a **floating widget** to any website.

---

## ⚡ Quick Integration (2 Minutes)

### **Option 1: Simple HTML (No Dependencies)**

Add this **one line** to your website's HTML (before closing `</body>` tag):

```html
<iframe id="sentinel-widget"
        src="http://localhost:5000/chatbot_widget.html"
        style="position: fixed; bottom: 20px; right: 20px; width: 0; height: 0; border: none; z-index: 9999;"
        allow="geolocation"></iframe>
```

**That's it!** The widget appears as a floating button automatically. 🚀

---

## 🔧 Advanced Integration

### **Option 2: With Configuration**

If your backend is on a different server/IP:

```html
<!-- Step 1: Configure the backend URL -->
<script>
    window.sentinelConfig = {
        backendUrl: "http://192.168.1.100:5000"  // Your backend server IP
    };
</script>

<!-- Step 2: Add the widget -->
<iframe id="sentinel-widget"
        src="http://192.168.1.100:5000/chatbot_widget.html"
        style="position: fixed; bottom: 20px; right: 20px; width: 0; height: 0; border: none; z-index: 9999;"
        allow="geolocation"></iframe>
```

---

## 📱 Full Website Example

Here's a complete example embedding the widget:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <!-- Your website content here -->
    <h1>Welcome to My Site</h1>
    <p>Your website content...</p>

    <!-- ADD THIS AT THE BOTTOM -->
    <script>
        window.sentinelConfig = {
            backendUrl: "http://localhost:5000"
        };
    </script>

    <iframe id="sentinel-widget"
            src="http://localhost:5000/chatbot_widget.html"
            style="position: fixed; bottom: 20px; right: 20px; width: 0; height: 0; border: none; z-index: 9999;"
            allow="geolocation"></iframe>

</body>
</html>
```

---

## 🎨 Customize Widget Position

### **Bottom Left Corner** (instead of bottom right):
```html
<iframe id="sentinel-widget"
        src="http://localhost:5000/chatbot_widget.html"
        style="position: fixed; bottom: 20px; left: 20px; width: 0; height: 0; border: none; z-index: 9999;"
        allow="geolocation"></iframe>
```

### **Top Right Corner**:
```html
<iframe id="sentinel-widget"
        src="http://localhost:5000/chatbot_widget.html"
        style="position: fixed; top: 20px; right: 20px; width: 0; height: 0; border: none; z-index: 9999;"
        allow="geolocation"></iframe>
```

### **Custom Distance from Edge**:
```html
<!-- 50px from bottom, 30px from right -->
<iframe id="sentinel-widget"
        src="http://localhost:5000/chatbot_widget.html"
        style="position: fixed; bottom: 50px; right: 30px; width: 0; height: 0; border: none; z-index: 9999;"
        allow="geolocation"></iframe>
```

---

## 🌐 Network Access

### **Same Computer**:
```html
<iframe src="http://localhost:5000/chatbot_widget.html" ...></iframe>
```

### **Same WiFi Network**:
First, find your server IP:
```bash
# Windows
ipconfig
# Look for IPv4 Address like: 192.168.1.100 or 10.0.0.5
```

Then use:
```html
<iframe src="http://192.168.1.100:5000/chatbot_widget.html" ...></iframe>
```

### **Over Internet (Public URL)**:
Use a service like **ngrok** to expose your local backend:
```bash
ngrok http 5000
```
Then use the generated URL:
```html
<iframe src="https://your-ngrok-url.ngrok.io/chatbot_widget.html" ...></iframe>
```

---

## 🔐 Security Notes

1. **API Key**: Keep your `GEMINI_API_KEY` secret in `ai_service.py` (never expose it in frontend code)
2. **CORS**: Already enabled in backend - frontend can call from any domain
3. **Rate Limiting**: Consider adding rate limits to `/chatbot` endpoint if public
4. **Authentication**: Add admin password for `/admin/*` endpoints if needed

---

## 🚀 Framework Integration Examples

### **React**
```jsx
import React, { useEffect } from 'react';

export default function ChatbotWidget() {
  useEffect(() => {
    window.sentinelConfig = {
      backendUrl: "http://localhost:5000"
    };
  }, []);

  return (
    <iframe
      id="sentinel-widget"
      src="http://localhost:5000/chatbot_widget.html"
      style={{
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        width: 0,
        height: 0,
        border: 'none',
        zIndex: 9999
      }}
      allow="geolocation"
    />
  );
}
```

### **Vue.js**
```vue
<template>
  <iframe
    id="sentinel-widget"
    :src="backendUrl + '/chatbot_widget.html'"
    style="position: fixed; bottom: 20px; right: 20px; width: 0; height: 0; border: none; z-index: 9999;"
    allow="geolocation"
  ></iframe>
</template>

<script>
export default {
  data() {
    return {
      backendUrl: 'http://localhost:5000'
    };
  },
  mounted() {
    window.sentinelConfig = {
      backendUrl: this.backendUrl
    };
  }
};
</script>
```

### **Next.js**
```jsx
import { useEffect } from 'react';

export default function Home() {
  useEffect(() => {
    window.sentinelConfig = {
      backendUrl: process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:5000'
    };
  }, []);

  return (
    <>
      <h1>My Site</h1>
      <iframe
        id="sentinel-widget"
        src={`${process.env.NEXT_PUBLIC_BACKEND_URL}/chatbot_widget.html`}
        style={{
          position: 'fixed',
          bottom: '20px',
          right: '20px',
          width: 0,
          height: 0,
          border: 'none',
          zIndex: 9999
        }}
        allow="geolocation"
      />
    </>
  );
}
```

---

## ✅ Testing the Widget

1. **Start backend**: `python ai_service.py`
2. **Open your website** in browser
3. **Look for floating red button** in bottom-right corner
4. **Click it** → Chat window opens
5. **Type a message** → AI responds ✅

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Widget not appearing | Check browser console (F12) for errors; verify backend URL |
| "Backend not connected" | Ensure `python ai_service.py` is running; check IP address |
| Widget hidden behind content | Increase `z-index` (9999 is default) |
| CORS errors in console | Backend already has CORS enabled; check URL format |
| Chat not responding | Verify Gemini API key in `ai_service.py` |

---

## 📊 Widget Features

- ✅ **Floating Button** - Colorful animated toggle
- ✅ **Chat History** - Saves in session
- ✅ **Unread Badge** - Shows count when closed
- ✅ **Disaster Type Selection** - 4 types (Medical, Flood, Earthquake, Fire)
- ✅ **Auto-resize** - Responsive on mobile
- ✅ **Smooth Animations** - Professional feel
- ✅ **Error Handling** - Shows clear error messages

---

## 🔗 Related Files

- `chatbot_widget.html` - Main widget file
- `ai_service.py` - Backend server
- `index.html` - Full-page version
- `admin_dashboard.html` - Admin tracking
- `README.md` - Main documentation

---

**Questions?** Check the main README.md or test locally first!

Happy embedding! 🎊
