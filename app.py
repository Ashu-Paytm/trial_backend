from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        headers = dict(request.headers)
        
        if not data:
            return jsonify({"error": "No JSON data received"}), 400
        
        # Process the data (you can customize this part)
        device_id = data.get("device_id", "Unknown")
        sensor_value = data.get("sensor_value", 0)
        nested_data = data.get("nested", {})
        
        print(f"Received data from device {device_id}: {sensor_value}")
        print(f"Nested Data: {nested_data}")
        print(f"Headers: {headers}")
        
        # Respond to the IoT device
        response = {
            "message": "Data received successfully",
            "device_id": device_id,
            "status": "OK",
            "received_headers": headers,
            "received_nested_data": nested_data
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    from gunicorn.app.wsgiapp import run
    run()
