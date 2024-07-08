from dotenv import load_dotenv
import requests
import json
import os
import base64

load_dotenv()

API_KEY = os.environ.get("API_KEY")

MANAGER_PHONE_NUMBER = os.environ.get("MANAGER_PHONE_NUMBER")

PRIMARY_CONTACT_NUMBER = os.environ.get("PRIMARY_CONTACT_NUMBER")

LIST_CONTACT_NUMBERS = os.environ.get("LIST_CONTACT_NUMBERS")

url = "https://app.whatsgw.com.br/api/WhatsGw/Send"

with open("./media/whatsgw.pdf", "rb") as pdf_file:
    pdf_binary_data = pdf_file.read()
    pdf_base64 = base64.b64encode(pdf_binary_data).decode("utf-8")

payload = json.dumps(
    {
        "apikey": API_KEY,
        "phone_number": MANAGER_PHONE_NUMBER,
        "contact_phone_number": PRIMARY_CONTACT_NUMBER,
        "message_custom_id": "yoursoftwareid",
        "message_type": "document",
        "check_status": "1",
        "message_body_mimetype": "application/pdf",
        "message_body_filename": "nome_documento.pdf",
        "message_caption": "texto que fica em baixo",
        "message_body": pdf_base64,
    }
)
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
