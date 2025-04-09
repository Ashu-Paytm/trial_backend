from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_any_data():
    try:
        print("🔔 POST request received!")

        # Log everything for debugging
        print(f"Headers: {dict(request.headers)}")
        print(f"Raw Body: {request.data.decode('utf-8', errors='ignore')}")

        return jsonify({
            "message": "POST request received",
            "status": "OK"
        }), 200
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Make sure it works on Render
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
