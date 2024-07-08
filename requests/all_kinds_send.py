from dotenv import load_dotenv
import requests
import json
import os
import base64


load_dotenv()

API_KEY = os.environ.get("API_KEY")

MANAGER_PHONE_NUMBER = os.environ.get("MANAGER_PHONE_NUMBER")

PRIMARY_CONTACT_NUMBER = os.environ.get("PRIMARY_CONTACT_NUMBER")

LIST_CONTACT_NUMBERS = os.environ.get("LIST_CONTACT_NUMBERS").split(",")

url = "https://app.whatsgw.com.br/api/WhatsGw/Send"


if not all([API_KEY, MANAGER_PHONE_NUMBER, PRIMARY_CONTACT_NUMBER, LIST_CONTACT_NUMBERS]):
    raise ValueError("Alguma variável de ambiente não foi configurada corretamente.")


def add_header_body(text, extension, mimetype, message_type):
    with open(f"./media/whatsgw{extension}", "rb") as doc_file:
        binary_data = doc_file.read()
        file_base64 = base64.b64encode(binary_data).decode("utf-8")

    header = {
        "message_type": message_type,
        "message_body_mimetype": mimetype,
        "message_body_filename": "nome_documento.pdf",
        "message_caption": text,
        "message_body": file_base64,
    }

    return header


file = True

texto = input("digite um texto personalizado para mensagem whats\n: ")

headers_body = {
    "apikey": API_KEY,
    "phone_number": MANAGER_PHONE_NUMBER,
    "contact_phone_number": LIST_CONTACT_NUMBERS[0],
    "message_custom_id": "yoursoftwareid",
    "message_type": "text",
    "message_body": texto,
}

if file is True:
    print("""
    diga o tipo de arquivo
    1 == document
    2 == audio
    3 == video
    4 == image""")
    message_type_input = abs(int(input("")))

    file_types = [
        {"type": "document", "extension": ".pdf", "mimetype": "application/pdf"},
        {"type": "ptt", "extension": ".ogg", "mimetype": "audio/ogg; codecs=opus"},
        {"type": "video", "extension": ".mp4", "mimetype": "video/mp4"},
        {"type": "image", "extension": "jpg", "mimetype": "image/jpeg"},
    ]
    
    file_type = file_types[message_type_input - 1]

    header = add_header_body(texto, file_type["extension"], file_type['mimetype'], file_type["type"])

    headers_body.update(header)

payload = json.dumps(headers_body)

headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
