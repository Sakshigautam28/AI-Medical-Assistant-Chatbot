import google.genai as genai
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import sys

# --- CONFIGURATION ---
# Replace with your actual key from Google AI Studio
GEMINI_API_KEY = "AIzaSyBbP54-GpyIMSJe7mtd5dhKZ8r7A8n9RAc" 
client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)
CORS(app)

# Session history storage (In-memory)
chat_histories = {}
victim_queue = []

@app.route('/', methods=['GET'])
def home():
    """Home route - shows server status"""
    return jsonify({
        "status": "online",
        "service": "Sentinel Alpha - Emergency Response AI",
        "version": "1.0",
        "endpoints": {
            "GET /index.html": "Main chatbot UI",
            "GET /admin_dashboard.html": "Admin victim tracking",
            "GET /chatbot_widget.html": "Embeddable widget",
            "POST /chatbot": "Get emergency guidance from AI",
            "POST /dispatch_volunteer": "Dispatch emergency SOS",
            "GET /admin/victims": "View all victims",
            "POST /admin/update_victim": "Update victim status"
        }
    })

@app.route('/index.html', methods=['GET'])
def serve_index():
    """Serve main chatbot UI"""
    return send_file('index.html', mimetype='text/html')

@app.route('/admin_dashboard.html', methods=['GET'])
def serve_admin():
    """Serve admin dashboard"""
    return send_file('admin_dashboard.html', mimetype='text/html')

@app.route('/chatbot_widget.html', methods=['GET'])
def serve_widget():
    """Serve embeddable widget"""
    return send_file('chatbot_widget.html', mimetype='text/html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_id = data.get('user_id', 'guest_user')
    message = data.get('symptoms', "")
    disaster_type = data.get('disaster', "general emergency")
    
    # Log to file
    with open('debug.log', 'a', encoding='utf-8') as f:
        f.write(f"\n[REQUEST] user={user_id} | disaster={disaster_type} | msg={message[:40]}\n")
    
    if user_id not in chat_histories:
        chat_histories[user_id] = []

    try:
        with open('debug.log', 'a', encoding='utf-8') as f:
            f.write(f"  -> Calling Gemini API...\n")
        
        # Create message with system instruction - asking for conversational Q&A format
        system_instruction = (
            f"You are Sentinel Alpha, emergency AI for {disaster_type}. "
            f"User reports: {message}. "
            f"Format your response as a real conversation:\n"
            f"1. Ask 2-3 clarifying questions to understand better\n"
            f"2. Then provide numbered first-aid steps\n"
            f"Keep it concise and conversational, not bullet points."
        )
        
        # Build conversation history for context
        history = chat_histories[user_id]
        
        # Create request with history
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=[
                {"role": "user", "parts": [{"text": system_instruction}]},
                {"role": "model", "parts": [{"text": "I'm Sentinel Alpha, ready to help with questions first."}]},
                *history,
                {"role": "user", "parts": [{"text": message}]}
            ]
        )
        
        with open('debug.log', 'a', encoding='utf-8') as f:
            f.write(f"  -> Got Gemini response ({len(response.text)} chars)\n")
        
        # Save to history
        chat_histories[user_id].append({"role": "user", "parts": [{"text": message}]})
        chat_histories[user_id].append({"role": "model", "parts": [{"text": response.text}]})
        
        return jsonify({"advice": [response.text.strip()]})

    except Exception as e:
        with open('debug.log', 'a', encoding='utf-8') as f:
            f.write(f"  -> ERROR: {type(e).__name__}: {str(e)[:300]}\n")
            import traceback
            f.write(f"  Traceback:\n{traceback.format_exc()}\n")
        
        # Check if it's a quota error
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e) or "quota" in str(e).lower():
            quota_msg = "⚠️ AI API QUOTA EXCEEDED\n\nThe Gemini API free tier limit (20 requests/day) has been reached.\n\nOptions:\n• Wait 45+ seconds and try again\n• Upgrade your API plan to https://ai.google.dev\n• Or use offline emergency guidance below"
            return jsonify({"advice": [quota_msg]})
        
        # Local fallback responses based on disaster type if API fails
        fallback_responses = {
            "medical": "• KEEP CALM: Ensure patient is comfortable and conscious\n• CHECK VITALS: Monitor breathing and pulse rate\n• CPR IF NEEDED: 100-120 compressions per minute if unconscious\n• CALL 911: Emergency services immediately\n• DO NOT MOVE: Unless in immediate danger",
            "fire": "• EVACUATE NOW: Use stairs only, never elevators\n• STAY LOW: Move below smoke level\n• CHECK DOORS: Touch before opening - if hot, find another exit\n• MOVE AWAY: From building perimeter immediately\n• DO NOT RETURN: Under any circumstances",
            "flood": "• MOVE UP: To higher ground as fast as possible\n• AVOID WATER: Never drive/walk through flooded areas\n• CLIMB HIGH: To roof or highest floor if trapped\n• GET ATTENTION: Wave bright cloth or signal for help\n• AVOID CONTACT: Floodwater is contaminated",
            "earthquake": "• DROP-COVER-HOLD: Immediately to hands and knees\n• PROTECT HEAD: Cover with arms under sturdy furniture\n• HOLD POSITION: Until shaking completely stops\n• AVOID WINDOWS: Stay away from glass and falling objects\n• CHECK INJURIES: After shaking stops completely",
            "storm": "• SEEK SHELTER: Interior room away from windows\n• CLOSE WINDOWS: Do not open - doesn't reduce damage\n• AVOID OUTDOORS: Stay away from trees and power lines\n• LIE LOW: In ditch if no shelter available\n• MONITOR ALERTS: Listen for weather warnings"
        }
        
        # Get fallback response based on disaster type
        fallback_msg = fallback_responses.get(disaster_type.lower(), fallback_responses["medical"])
        return jsonify({"advice": [fallback_msg]})
        
        # Local fallback responses based on disaster type if API fails
        fallback_responses = {
            "medical": "• KEEP CALM: Ensure patient is comfortable and conscious\n• CHECK VITALS: Monitor breathing and pulse rate\n• CPR IF NEEDED: 100-120 compressions per minute if unconscious\n• CALL 911: Emergency services immediately\n• DO NOT MOVE: Unless in immediate danger",
            "fire": "• EVACUATE NOW: Use stairs only, never elevators\n• STAY LOW: Move below smoke level\n• CHECK DOORS: Touch before opening - if hot, find another exit\n• MOVE AWAY: From building perimeter immediately\n• DO NOT RETURN: Under any circumstances",
            "flood": "• MOVE UP: To higher ground as fast as possible\n• AVOID WATER: Never drive/walk through flooded areas\n• CLIMB HIGH: To roof or highest floor if trapped\n• GET ATTENTION: Wave bright cloth or signal for help\n• AVOID CONTACT: Floodwater is contaminated",
            "earthquake": "• DROP-COVER-HOLD: Immediately to hands and knees\n• PROTECT HEAD: Cover with arms under sturdy furniture\n• HOLD POSITION: Until shaking completely stops\n• AVOID WINDOWS: Stay away from glass and falling objects\n• CHECK INJURIES: After shaking stops completely",
            "storm": "• SEEK SHELTER: Interior room away from windows\n• CLOSE WINDOWS: Do not open - doesn't reduce damage\n• AVOID OUTDOORS: Stay away from trees and power lines\n• LIE LOW: In ditch if no shelter available\n• MONITOR ALERTS: Listen for weather warnings"
        }
        
        # Get fallback response based on disaster type
        fallback_msg = fallback_responses.get(disaster_type.lower(), fallback_responses["medical"])
        return jsonify({"advice": [fallback_msg]})

@app.route('/dispatch_volunteer', methods=['POST'])
def dispatch_volunteer():
    data = request.json
    victim_entry = {
        "id": len(victim_queue) + 1,
        "symptoms": data.get('symptoms'),
        "lat": data.get('lat'),
        "lng": data.get('lng'),
        "disaster": data.get('disaster', 'general'),
        "status": "UNASSIGNED",
        "timestamp": __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    victim_queue.append(victim_entry)
    print(f"📢 SOS RECEIVED: Victim #{victim_entry['id']} at {victim_entry['lat']}, {victim_entry['lng']}")
    return jsonify({"status": "success", "victim_id": victim_entry['id']})

@app.route('/admin/victims', methods=['GET'])
def get_all_victims():
    """Admin endpoint to view all active victims"""
    return jsonify({
        "total_victims": len(victim_queue),
        "victims": victim_queue
    })

@app.route('/admin/update_victim', methods=['POST'])
def update_victim_status():
    """Admin endpoint to update victim status"""
    data = request.json
    victim_id = data.get('victim_id')
    new_status = data.get('status')  # e.g., "ASSIGNED", "IN_PROGRESS", "RESOLVED"
    
    for victim in victim_queue:
        if victim['id'] == victim_id:
            victim['status'] = new_status
            print(f"✅ Victim #{victim_id} status updated to {new_status}")
            return jsonify({"status": "success", "message": f"Victim updated to {new_status}"})
    
    return jsonify({"status": "error", "message": "Victim not found"}), 404

if __name__ == '__main__':
    # host='0.0.0.0' makes it accessible on your Wi-Fi network
    # Port 5000 is standard for Flask
    print("🟢 Sentinel Alpha Server Starting...")
    print("📍 Access locally at: http://localhost:5000")
    print("📍 Access from WiFi at: http://10.2.8.241:5000")
    print("⚠️  Note: Gemini API calls require internet (may be blocked by your WiFi)")
    print("")
    app.run(debug=True, host='0.0.0.0', port=5000)