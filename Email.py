import smtplib

sender = "akinloyeifeoluwa46@gmail.com"
receiver = "tobiakinz@gmail.com"
subject = "Python Email Test"
password = "mcdarella"
body = "My First python Email"

#THIS IS THE HEADER
message = f""" From: Ifeoluwa Akinloye{sender}
To: Oluwatobiloba Akinloye{receiver}
Subject: {subject}\n
{body}
"""
# THIS IS FOR THE SERVER OR SERVER OBJECT
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")