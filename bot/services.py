import os
import requests

PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
TOKEN = os.getenv("WHATSAPP_TOKEN")


def send_main_menu(phone):

    payload = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "اختر الخدمة المطلوبة"
            },
            "action": {
                "button": "عرض الخدمات",
                "sections": [
                    {
                        "title": "الخدمات الرئيسية",
                        "rows": [
                            {
                                "id": "consultation",
                                "title": "استشارة هندسية مجانية"
                            },
                            {
                                "id": "design",
                                "title": "تصميم مخططات هندسية"
                            },
                            {
                                "id": "supervision",
                                "title": "إشراف هندسي"
                            },
                            {
                                "id": "other_services",
                                "title": "خدمات أخرى"
                            }
                        ]
                    }
                ]
            }
        }
    }

    requests.post(
        f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        },
        json=payload,
    )