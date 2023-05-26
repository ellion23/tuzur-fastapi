import smtplib
from random import randint
from config import smtp_password

email = 'service.ellion23@internet.ru'
code = f"{randint(1, 9999):04d}"
smtp_server = 'smtp.mail.ru:465'


dest_email = 'rubcinskija@gmail.com'
subject = 'Restore password'
body = 'Use that code: ' + code + " to restore your password."

letter = f"""\
From: {email}
To: {dest_email}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";
{body}"""
letter = letter.encode("UTF-8")


server = smtplib.SMTP_SSL(smtp_server)
server.login(email, smtp_password)
server.sendmail(email, dest_email, letter)
server.quit()

class EmailService:
    def __init__(self):
        pass
