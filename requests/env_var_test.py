from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")

MANAGER_PHONE_NUMBER = os.environ.get("MANAGER_PHONE_NUMBER")

PRIMARY_CONTACT_NUMBER = os.environ.get("PRIMARY_CONTACT_NUMBER")

LIST_CONTACT_NUMBERS = os.environ.get("LIST_CONTACT_NUMBERS")

MESSAGE_TYPES = os.environ.get("MESSAGE_TYPES")
FILES_EXTENSION = os.environ.get("FILES_EXTENSION")
MIMETYPES = os.environ.get("MIMETYPES")

lista_numeros = LIST_CONTACT_NUMBERS.split(",")

message_types = MESSAGE_TYPES.split(",")
files_extension = FILES_EXTENSION.split(",")
mimetypes = MIMETYPES.split(",")

print(API_KEY)
print(MANAGER_PHONE_NUMBER)
print(PRIMARY_CONTACT_NUMBER)
print(lista_numeros)
print(message_types)
print(files_extension)
print(mimetypes)
