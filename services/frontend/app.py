from flask import Flask, jsonify, render_template_string
import requests
import os

app = Flask(__name__)

# Backend service URL
# In Kubernetes this will be the backend service name
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:5001')

# Main page
@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MediTrack</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                max-width: 800px; 
                margin: 50px auto; 
                background-color: #f0f4f8;
            }
            h1 { color: #2c5282; }
            .card {
                background: white;
                padding: 20px;
                border-radius: 8px;
                margin: 20px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .healthy { color: green; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>🏥 MediTrack Health System</h1>
        <div class="card">
            <h2>System Status</h2>
            <p class="healthy">✅ Frontend Service: Running</p>
        </div>
        <div class="card">
            <h2>Quick Links</h2>
            <p><a href="/health">Frontend Health Check</a></p>
            <p><a href="/patients">View Patients</a></p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "meditrack-frontend",
        "version": "1.0.0"
    })

# Patients page
@app.route('/patients')
def patients():
    try:
        response = requests.get(f'{BACKEND_URL}/patients', timeout=5)
        data = response.json()
        return jsonify({
            "source": "backend-api",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "source": "backend-api",
            "error": "Could not connect to backend",
            "details": str(e)
        }), 503

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)