from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

# Route to serve index.html
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_email():
    data = request.json
    topic = data.get("topic")
    link = data.get("link")
    desc = data.get("desc")

    # Compose the email
    msg = EmailMessage()
    msg["Subject"] = f"New Submission: {topic}"
    msg["From"] = "your-email@gmail.com"
    msg["To"] = "receiver-email@gmail.com"
    msg.set_content(f"Link: {link}\n\nDescription: {desc}")

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("your-email@gmail.com", "your-app-password")
        smtp.send_message(msg)

    return jsonify({"message": "Email sent successfully!"}), 200
