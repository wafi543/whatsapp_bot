import json
import os
import requests

PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
TOKEN = os.getenv("WHATSAPP_TOKEN")


def send_menu(phone, menu_file):
    # Load menu from JSON file
    file_path = os.path.join(os.path.dirname(__file__), 'menus', menu_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        payload = json.load(f)
    
    # Add phone number to payload
    payload['to'] = phone

    requests.post(
        f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        },
        json=payload,
    )