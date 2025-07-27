
from flask import Flask, request, jsonify
from mailer import send_email  # this is your email.py

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    topic = data.get('topic')
    link = data.get('link')
    des = data.get('des', '')
    
    if not topic or not link:
        return "❌ Topic and Link are required!", 400
    
    try:
        send_email(topic, link, des)
        return "✅ Email sent successfully!"
    except Exception as e:
        return f"❌ Failed to send email: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
