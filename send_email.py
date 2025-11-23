import smtplib
from email.mime.text import MIMEText

sender="abcdef@gmail.com"
receiver="ghijkl@gmail.com"
password="YOUR_APP_PASSWORD" #Use app password NOT Gmail password

msg=MIMEText("Hello Deep!I hope you're doing well. I just wanted to share that I’ve started learning Python recently.I’ll keep practicing daily and will update you with more progress soon.")
msg["Subject"]="Python Automation Test"
msg["From"]=sender
msg["To"]=receiver

with smtplib.SMTP("smtp.gmail.com",587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
print("Email Sent Successfully.")
