# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from datetime import datetime
# import os

# # Optional: Use environment variables for sensitive data
# # You can create a .env file and use dotenv to load this securely
# sender_email = "dhruvjain20102004@gmail.com"
# receiver_email = "dj20101004@gmail.com"
# password = "hxdv zwxt ufhj nfiv"  # For better security, store this in an environment variable
from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

EMAIL_ADDRESS = "dhruvjain20102004@gmail.com"      # replace with your email
EMAIL_PASSWORD = "hxdv zwxt ufhj nfiv"   

# use app password (not Gmail password)
def day():
    from datetime import datetime
    return (datetime.today() - datetime(2025, 7, 4)).days 

@app.route('/send', methods=['POST'])
def send_email():
    data = request.get_json()
    topic = data.get('topic')
    link = data.get('link')
    desc = data.get('desc')

    msg = EmailMessage()
    msg['Subject'] = "Day" + str(day())
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = "dj20101004@gmail.com"   # change to receiver's email
    if desc=="" or desc=="": 
        msg.set_content(f"Good Evening Ma'am, \n\t Today's GD Topic: {topic}\n\tLink: {link}\nThank you Ma'am.")
    else:
        msg.set_content(f"Good Evening Ma'am, \n\t Today's GD Topic: {topic}\n\tLink: {link}\n\t {desc}. \nThank you Ma'am.")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
