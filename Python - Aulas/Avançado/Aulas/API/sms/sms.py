from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
import os

load_dotenv()

# Your Account SID and Auth Token from console.twilio.com
account_sid = os.getenv('ACCOUNT_SID')
auth_token  = os.getenv('API_KEY')

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5511999999999",
    from_="+15017122661",
    body="Teste de envio",
)


print(message.sid)
