from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        headers = dict(request.headers)
        content_type = request.content_type or ""

        if 'application/json' in content_type:
            data = request.get_json(silent=True)
            if not data:
                return jsonify({"error": "No JSON data received"}), 400

            device_id = data.get("deviceId", "Unknown")
            logs = data.get("logs", "")
            timestamp = data.get("timestamp", "N/A")
            log_type = data.get("type", "Unknown")

            print(f"Received logs from device {device_id}")
            print(f"Type: {log_type}")
            print(f"Timestamp: {timestamp}")
            print(f"Logs (base64): {logs}")
        else:
            raw_data = request.data.decode('utf-8', errors='ignore')
            print(f"Received RAW data: {raw_data}")

            device_id = "Unknown"
            logs = raw_data
            timestamp = "N/A"
            log_type = "Unknown"

        print(f"Headers: {headers}")

        response = {
            "message": "Log data received successfully",
            "device_id": device_id,
            "status": "OK",
            "log_type": log_type,
            "timestamp": timestamp,
            "received_headers": headers,
            "logs": logs if 'application/json' in content_type else None,
            "raw_data": logs if 'application/json' not in content_type else None
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    from gunicorn.app.wsgiapp import run
    run()
