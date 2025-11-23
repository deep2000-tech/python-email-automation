# Python Email Automation using smtplib

This project demonstrates how to send emails automatically using Python's built-in `smtplib` and `email.mime.text.MIMEText` libraries. The script allows you to send a plain-text email to any recipient using Gmail’s SMTP server.

---

## Features

- Sends automated email with a subject and message.
- Uses Gmail SMTP server.
- Beginner-friendly and easy to modify.
- Uses **App Password** instead of normal Gmail password (for security).

---

## Requirements

- Python 3.8 or higher
- Internet connection
- Gmail account with **App Password enabled**

---

## Gmail Security Setup

Google no longer allows login using normal Gmail passwords in scripts.  
To use this project, follow these steps:

1. Enable **2-Step Verification** in your Google account.
2. Create a **16-digit App Password** here:  
   👉 https://myaccount.google.com/apppasswords
3. Replace the placeholder password in the code with the generated app password.

---

## Code Example

```python
import smtplib
from email.mime.text import MIMEText

sender = "your_email@gmail.com"
receiver = "receiver_email@gmail.com"
password = "YOUR_APP_PASSWORD"  # Use App Password NOT Gmail password

msg = MIMEText("Hello! I hope you're doing well. This is a Python email automation test.")
msg["Subject"] = "Python Automation Test"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())

print("Email Sent Successfully.")
