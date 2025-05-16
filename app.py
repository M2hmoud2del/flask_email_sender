from flask import Flask
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def send_email(recipient_email, subject, message_body):
    with app.app_context():
        msg = Message(
            subject=subject,
            sender=app.config['MAIL_USERNAME'],
            recipients=[recipient_email],
            body=message_body
        )
        mail.send(msg)
        print(f"Email sent to {recipient_email}")

if __name__ == "__main__":
    recipient = input("Recipient Email: ")
    subject = input("Subject: ")
    body = input("Message Body: ")
    send_email(recipient, subject, body)
