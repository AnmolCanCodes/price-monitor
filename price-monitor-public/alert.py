import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(html_content, sender, password, receiver):
    msg = MIMEMultipart()
    msg["Subject"] = "E-commerce Monitoring Report"
    msg["From"] = sender
    msg["To"] = receiver

    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())