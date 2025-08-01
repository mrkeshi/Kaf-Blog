import json
from ipware import get_client_ip as ipware_get_client_ip

from django.conf import settings
from pywebpush import webpush, WebPushException

from Setting.models import NotificationSubscription


def get_client_ip(request):
    ip, is_routable = ipware_get_client_ip(request)

    return ip

def send_push_to_all(title: str, body: str, url: str):
    url= f"{settings.BASE_URL}{url}"
    subscriptions = NotificationSubscription.objects.all()
    vapid_private_key = settings.VAPID_PRIVATE_KEY

    payload = {
        "title": title,
        "body": body,
        "url": url
    }

    for sub in subscriptions:
        try:
            webpush(
                subscription_info=sub.subscription_info,
                data=json.dumps(payload),
                vapid_private_key=vapid_private_key,
                vapid_claims={
                    "sub": "mailto:admin@example.com"
                }
            )
            print("\n \n SUCCESS SENDING NOT \n \n")
        except WebPushException as ex:
            print(f"⚠️ خطا در ارسال نوتیف به {sub}: {repr(ex)}")