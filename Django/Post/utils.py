import json

import pytz
from ipware import get_client_ip as ipware_get_client_ip

from django.conf import settings
from jalali_date import date2jalali
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
            if ex.response and ex.response.status_code in [404, 410]:
                print(f"اشتراک منقضی شده یا نامعتبر، حذف می‌شود: {sub}")
                sub.delete()
            else:
                print(f"⚠️ خطا در ارسال نوتیف به {sub}: {repr(ex)}")

def jalali_converter(datetime_obj):
    local_time = datetime_obj.astimezone(pytz.timezone('Asia/Tehran'))
    jalali_date = date2jalali(local_time)
    months = [
        "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
        "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
    ]
    year = jalali_date.year
    month_name = months[jalali_date.month - 1]
    day = jalali_date.day
    hour = local_time.hour
    minute = local_time.minute
    return f"{day} {month_name} {year} - {hour:02d}:{minute:02d}"