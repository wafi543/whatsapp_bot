from django.urls import path
from bot.views import webhook

urlpatterns = [
    path("webhook/", webhook),
]