import json
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

VERIFY_TOKEN = os.getenv("WEBHOOK_VERIFY_TOKEN", "your-token")


@csrf_exempt
def webhook(request):

    if request.method == "GET":
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if token == VERIFY_TOKEN:
            return JsonResponse(challenge, safe=False)

        return JsonResponse({"error": "invalid token"}, status=403)

    if request.method == "POST":
        payload = json.loads(request.body)

        print(payload)

        return JsonResponse({"status": "ok"})