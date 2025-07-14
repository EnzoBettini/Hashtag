from imap_tools import MailBox, AND
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL_SENDER")
EMAIL_CC = os.getenv("EMAIL_CC")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

meu_email = MailBox('imap.gmail.com').login(EMAIL, EMAIL_PASSWORD)

lista_emails = meu_email.fetch(AND(from_=EMAIL, to=EMAIL_CC))

for email in lista_emails:
    print(email.subject)
    print(email.text)
    for anexo in email.attachments:
        with open(fr'C:\Users\enzo.bettini\Documents\Hashtag\Python - Aulas\Avançado\email\Copy - {anexo.filename}', 'wb') as copia_local:
            copia_local.write(anexo.payload)
