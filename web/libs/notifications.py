import os
import cv2

# Email libs
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Text libs
from email.message import EmailMessage

# Global vars
EMAIL = str(os.environ.get('EMAIL'))
EMAIL_PASSWD = str(os.environ.get('EMAIL_PASSWD'))
CARRIER = str(os.environ.get('CARRIER'))
PHONE_NUM = str(os.environ.get('PHONE_NUM'))
HOST = "smtp.gmail.com"
CARRIER_MAP = {
    "verizon": "vtext.com",
    "tmobile": "tmomail.net",
    "sprint": "messaging.sprintpcs.com",
    "at&t": "txt.att.net",
    "boost": "smsmyboostmobile.com",
    "cricket": "sms.cricketwireless.net",
    "uscellular": "email.uscc.net",
}

def send_email(sub, msg, img):
    # Email content
    subject = f"{sub}"
    body = f"{msg}"

    # Create message
    message = MIMEMultipart()
    message["From"] = EMAIL
    message["To"] = EMAIL
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # If there is an image attach it to the message
    if img is not None:
        img_bytes = cv2.imencode('.jpg', img)[1].tobytes() # convert img data to bytes
        image_part = MIMEImage(img_bytes, name="image.jpg")
        message.attach(image_part)

    # Connect to SMTP server
    with smtplib.SMTP(HOST, 587) as server:
        server.starttls()
        server.login(EMAIL, EMAIL_PASSWD)
        text = message.as_string()
        server.sendmail(EMAIL, EMAIL, text)

def send_text(sub, msg, img):
    to_email = CARRIER_MAP[CARRIER]

    # Create message
    message = EmailMessage()
    message["From"] = EMAIL
    message["To"] = f"{PHONE_NUM}@{to_email}"
    message["Subject"] = sub
    message.set_content(msg)

    # NOTE: images via text not working at the moment
    # If there is an image attach it to the message
    if img is not None:
        img_bytes = cv2.imencode('.jpg', img)[1].tobytes() # convert img data to bytes
        message.add_attachment(img_bytes, maintype="image", subtype="jpg", filename="image.jpg")

    # Connect to SMTP server
    with smtplib.SMTP(HOST, 587) as server:
        server.starttls()
        server.login(EMAIL, EMAIL_PASSWD)
        server.send_message(message)