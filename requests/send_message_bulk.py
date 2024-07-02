from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")

MANAGER_PHONE_NUMBER = os.environ.get("MANAGER_PHONE_NUMBER")

PRIMARY_CONTACT_NUMBER = os.environ.get("PRIMARY_CONTACT_NUMBER")

LIST_CONTACT_NUMBERS = os.environ.get("LIST_CONTACT_NUMBERS")

url = "https://app.whatsgw.com.br/api/WhatsGw/SendBulk"

lista_requests = LIST_CONTACT_NUMBERS

for x in range(1, 2):
    lista_requests.append(
        {
            "apikey": API_KEY,
            "phone_number": MANAGER_PHONE_NUMBER,
            "contact_phone_number": PRIMARY_CONTACT_NUMBER,
            "message_custom_id": "yoursoftwareid",
            "message_type": "text",
            "message_body": f"Teste de Msg {x}",
            "check_status": "1",
        },
    )

payload = json.dumps(lista_requests)

headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
