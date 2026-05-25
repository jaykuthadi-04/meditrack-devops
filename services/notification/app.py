from flask import Flask, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

# Store notifications in memory
# In production this would be a database
notifications = []

# Health check
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "meditrack-notification",
        "version": "1.0.0"
    })

# Get all notifications
@app.route('/notifications')
def get_notifications():
    return jsonify({
        "notifications": notifications,
        "total": len(notifications)
    })

# Send a notification
@app.route('/notify', methods=['POST'])
def send_notification():
    data = request.get_json()
    notification = {
        "id": len(notifications) + 1,
        "message": data.get('message', 'No message'),
        "recipient": data.get('recipient', 'Unknown'),
        "timestamp": datetime.now().isoformat(),
        "status": "sent"
    }
    notifications.append(notification)
    return jsonify({
        "success": True,
        "notification": notification
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port)