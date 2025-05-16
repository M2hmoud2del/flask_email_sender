from flask_mail import Mail, Message
from flask import Flask

def send_email(recipient_email, subject, message_body):
    app = Flask(__name__)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = "" 
    app.config['MAIL_PASSWORD'] = ""
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail = Mail(app)

    with app.app_context():
        msg = Message(
            subject=subject,
            sender=app.config['MAIL_USERNAME'],
            recipients=[recipient_email],
            body=message_body
        )
        mail.send(msg)
        print(f"Email sent to {recipient_email}")
