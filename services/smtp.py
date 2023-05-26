import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import smtp_password


class EmailService:
    def __init__(self) -> None:
        self.server = smtplib.SMTP_SSL('smtp.mail.ru:465')
        self.email = 'service.ellion23@internet.ru'

    def send_restore_code(self, dest_email: str, code: str) -> None:
        subject = 'Restore password'
        body = 'Use that code: ' + code + " to restore your password."

        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = dest_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        msg = msg.as_string()

        self.server.login(self.email, smtp_password)
        self.server.sendmail(self.email, dest_email, msg)
        self.server.quit()


email_service = EmailService()
