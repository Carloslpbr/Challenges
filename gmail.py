import os
from string import Template
from dotenv import load_dotenv 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pathlib

load_dotenv()

#caminho arquivo
CAMINHO_HTML = pathlib.Path(__file__).parent / 'gmail.html'

#dados do remetente e destinatário
origin = os.getenv('FROM_EMAIL','')
destination = origin

#configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL','')
smtp_password = os.getenv('EMAIL_PASSWORD','')

#mensagem de texto
with open(CAMINHO_HTML, 'r', encoding = 'utf-8') as file:
    text = file.read()
    template = Template(text)
    text_email = template.substitute(nome = 'Carlos')

#Transformar mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = origin
mime_multipart['to'] = destination
mime_multipart['subject'] = "Teste"

email_body = MIMEText(text_email, 'html', 'utf-8')
mime_multipart.attach(email_body)


#Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso')

