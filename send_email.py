import smtplib
from email.message import EmailMessage
import ssl

def send_email_alert(subject, body, attachment_path=None):
    sender = "sender email"
    app_password = "app password"
    receiver = "recievers email"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body)

    # Add image attachment
    if attachment_path:
        with open(attachment_path, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename=file_name)

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)
