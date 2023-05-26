import smtplib
from pydantic import EmailStr

from config import smtp_password

email = 'service.ellion23@internet.ru'
smtp_server = 'smtp.mail.ru:465'


class EmailService:
    def __init__(self):
        self.server = smtplib.SMTP_SSL(smtp_server)

    def send_restore_code(self, dest_email: EmailStr, code: str):
        subject = 'Restore password'
        body = 'Use that code: ' + code + " to restore your password."
        letter = f"""\
        From: {email}
        To: {dest_email}
        Subject: {subject}
        Content-Type: text/plain; charset="UTF-8";
        {body}"""
        letter = letter.encode("UTF-8")

        self.server.login(email, smtp_password)
        self.server.sendmail(email, dest_email, letter)
        self.server.quit()


email_service = EmailService
