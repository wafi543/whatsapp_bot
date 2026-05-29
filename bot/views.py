import json
import os

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

VERIFY_TOKEN = os.getenv("WEBHOOK_VERIFY_TOKEN")


@csrf_exempt
def webhook(request):

    if request.method == "GET":
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if token and token == VERIFY_TOKEN:
            return HttpResponse(challenge)

        return HttpResponse("Forbidden", status=403)

    elif request.method == "POST":
        payload = json.loads(request.body)

        print("WEBHOOK RECEIVED")
        print(json.dumps(payload, indent=2))

        return JsonResponse({"status": "ok"})

    return HttpResponse("Method not allowed", status=405)