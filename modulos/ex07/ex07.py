import os, smtplib, ssl
from pathlib import Path
from dotenv import load_dotenv  # type: ignore
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


PATH_HTML = Path(__file__).parent / "ex07.html"

load_dotenv()

smtp_server = os.getenv("SMTP_SERVER", "")
smtp_user = os.getenv("FROM_EMAIL", "")
smtp_password = os.getenv("PASSWORD_EMAIL", "")
smtp_port = 587

from_ = os.getenv("FROM_EMAIL", "")
to_ = from_

with open(PATH_HTML, "r", encoding="utf8") as file:
    file_text = file.read()
    template = Template(file_text).substitute(name="Fulano")

mime_multipart = MIMEMultipart()
mime_multipart["from"] = from_
mime_multipart["to"] = to_
mime_multipart["subject"] = "Um assunto qualquer."

mime_text = MIMEText(template, "html", "utf-8")
mime_multipart.attach(mime_text)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    #é como iniciar a conversa com o servidor
    server.ehlo()

    #só faz conexões com o servidor se houver segurança
    context = ssl.create_default_context()
    #para conexão segura
    server.starttls(context=context)

    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
