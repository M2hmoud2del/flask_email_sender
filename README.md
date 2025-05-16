تمام يا محمود، بما إنك ناوي **تضيف ملف `.env` في الـ commit**، يبقى لازم أعدّل التعليق في قسم "Project Structure" علشان يبقى واضح ومطابق.

وأنبهك إن دي **مش ممارسة آمنة** لو هترفع الريبو على GitHub، خصوصًا لو فيه بيانات حقيقية (زي بريدك أو كلمة السر)، بس لو لغرض تعليمي ومفيش بيانات حساسة، مفيش مشكلة.

إليك النسخة المعدّلة من `README.md`:

---

````markdown
# Flask Email Sender (CLI Tool)

A simple command-line Python tool to send emails using Flask-Mail.

This project demonstrates how to configure and use Flask-Mail to send emails via Gmail's SMTP server, with credentials loaded securely from environment variables.

## Features

- Send plain text emails using a Gmail account.
- CLI-based input (no HTML or frontend needed).
- Uses a `.env` file for credentials.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask_email_sender.git
cd flask_email_sender
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a file named `.env` in the root of the project and add your Gmail credentials:

```env
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
```

Important: If you have 2FA enabled on your Gmail account, you will need to use an App Password instead of your regular password. You can generate one from your Google Account settings.

## Usage

Run the program:

```bash
python app.py
```

You will be prompted to enter:

* Recipient email
* Email subject
* Email body

Example:

```
Recipient Email: test@example.com
Subject: Hello
Message Body: This is a test email.
```

## Project Structure

```
flask_email_sender/
├── app.py              # Main script to send email
├── .env                # Environment variables
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## License

This project is open source and free to use under the MIT License.

## Author

Developed by Mahmoud Adel
GitHub: [https://github.com/M2hmoud2del](https://github.com/M2hmoud2del)
LinkedIn: [https://www.linkedin.com/in/mahmoud-adel-975026127/](https://www.linkedin.com/in/mahmoud-adel-975026127/)
Website: [https://mahmoudadel.social-networking.me](https://mahmoudadel.social-networking.me/)