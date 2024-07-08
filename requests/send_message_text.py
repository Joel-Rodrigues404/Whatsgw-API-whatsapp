from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")

MANAGER_PHONE_NUMBER = os.environ.get("MANAGER_PHONE_NUMBER")

PRIMARY_CONTACT_NUMBER = os.environ.get("PRIMARY_CONTACT_NUMBER")

LIST_CONTACT_NUMBERS = os.environ.get("LIST_CONTACT_NUMBERS")

url = "https://app.whatsgw.com.br/api/WhatsGw/Send"

lista_numeros = LIST_CONTACT_NUMBERS.split(",")

payload = json.dumps(
    {
        "apikey": API_KEY,
        "phone_number": MANAGER_PHONE_NUMBER,
        "contact_phone_number": lista_numeros[0],
        # "contact_phone_number": PRIMARY_CONTACT_NUMBER,
        "message_custom_id": "yoursoftwareid",
        "message_type": "text",
        "message_body": "Mensagem teste",
    },
)
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)