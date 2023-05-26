import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Параметры подключения к серверу Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_password'

# Создаем объект MIMEMultipart для отправки письма
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = 'recipient_email@example.com'
msg['Subject'] = 'Тема письма'

# Добавляем текст письма
body = 'Текст письма'
msg.attach(MIMEText(body, 'plain'))

# Создаем SMTP-сессию и отправляем письмо
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, 'recipient_email@example.com', msg.as_string())

# Важно заменить smtp_username и smtp_password на свой адрес электронной почты и пароль соответственно.
# Также необходимо указать адрес получателя в строке msg['To'].
