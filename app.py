import os
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dahod_minibus_secret_key_2026'

# Threading mode is explicitly set to ensure local Anaconda runtime stability
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

active_drivers = {}
DRIVER_PASSWORD = "dahod2026"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/driver')
def driver_portal():
    return render_template('driver.html')

@app.route('/api/driver/login', methods=['POST'])
def driver_login():
    data = request.json or {}
    bus_number = data.get('bus_number', '').strip().upper()
    route_name = data.get('route_name', '')
    password = data.get('password', '')
    
    if not bus_number or not route_name:
        return jsonify({"success": False, "message": "Please enter valid credentials"}), 400
        
    if password != DRIVER_PASSWORD:
        return jsonify({"success": False, "message": "Incorrect Driver Password"}), 401
        
    return jsonify({"success": True, "message": "Authenticated successfully"})

@app.route('/api/driver/ping', methods=['POST'])
def process_mobile_telemetry():
    data = request.json or {}
    bus_id = data.get('bus_id', '').strip().upper()
    route = data.get('route')
    lat = data.get('latitude')
    lng = data.get('longitude')
    
    if not bus_id or lat is None or lng is None:
        return jsonify({"error": "Malformed telemetry packet"}), 400
        
    active_drivers[bus_id] = {
        "latitude": lat,
        "longitude": lng,
        "route": route
    }
    
    socketio.emit('fleet_update', {
        'bus_id': bus_id,
        'route': route,
        'latitude': float(lat),
        'longitude': float(lng),
        'active_count': len(active_drivers)
    })
    
    return jsonify({"status": "live"}), 200

if __name__ == '__main__':
    # Render assigns a port dynamically via environment variables
    port = int(os.environ.get("PORT", 5002))
    
    # Use 0.0.0.0 to listen to external production traffic
    socketio.run(app, host='0.0.0.0', port=port)