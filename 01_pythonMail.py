from email.message import EmailMessage
from cred import email, password
import ssl, smtplib


email_sender = email
email_password = password
email_receiver = 'sev3ncrows@gmail.com'

subject = "Hiii Sid!!"
body = """
Hiii Sid It's Email From Python!!!
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



    # msg = 'Your New Password is : '+PSWORD
    #         send_mail(
    #             'New Password',
    #             msg,
    #             settings.EMAIL_HOST_USER,
    #             [request.POST['email']],
    #             fail_silently=False,
    #         )
