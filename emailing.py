import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "dzcpzaobkswprnyw"
MY_MAIL = "anirudhhan.ashok@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Someone Detected!!"
    email_message.set_content("Hey, we just detected Someone👀!")

    with open(image_path, "rb") as file:
        content = file.read()
    
    email_message.add_attachment(content, maintype= "image",subtype = imghdr.what(None, content))

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg=email_message.as_string())

