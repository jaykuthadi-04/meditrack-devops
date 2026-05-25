from flask import Flask, jsonify
import os

app = Flask(__name__)

# Health check endpoint
# This is used by Kubernetes to check if the service is running
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "meditrack-backend",
        "version": "1.0.0"
    })

# Patients endpoint
# Returns dummy patient data
@app.route('/patients')
def patients():
    return jsonify({
        "patients": [
            {"id": 1, "name": "John Smith", "program": "Medicaid"},
            {"id": 2, "name": "Jane Doe", "program": "Medicare"},
            {"id": 3, "name": "Bob Johnson", "program": "SNAP"}
        ],
        "total": 3
    })

# Main entry point
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)