import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()

def EnvioCorreo(toEmail, Subject, BodyMail):
    #Configuration of mail
    fromEmail = os.getenv("MAIL")
    password = os.getenv("APPPASWORD")

    email = EmailMessage()

    email["From"] = fromEmail
    email["To"] = toEmail
    email["Subject"] = Subject
    email.set_content(BodyMail)

    #Ssl
    context = ssl.create_default_context()

    print("Correo por enviar")

    try:
        #Connection with SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(fromEmail, password)
            smtp.sendmail(fromEmail, toEmail, email.as_string())
            print("correo enviado")
        return 1
    
    except smtplib.SMTPRecipientsRefused:
        print("correo destinatario erroneo")
        return 0

    

EnvioCorreo("faxar36118@dacgu.com", "Test 10", "Prueba de correo")