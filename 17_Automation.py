from email.message import EmailMessage
from cred import email, password
import ssl, smtplib
import schedule
import time

def sndMail():
    email_sender = email
    email_password = password
    email_receiver = 'supermanishkeshav98@gmail.com'

    subject = "Hiii Manish!!"
    body = """
    Hiii Manish It's Email From Python!!!
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


# schedule.every().day.at('06:00').do(sndMail)

schedule.every(10).seconds.do(sndMail)

while True:
    schedule.run_pending()
    time.sleep(1)