import json

from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Post.utils import get_client_ip
from Setting.models import About, SiteSetting,Links,NotificationSubscription
from Setting.serializers import AboutSerializer, SettingSerializer,LinksSerializer,NotificationSubscriptionCountSerializer,NotificationSubscriptionCreateSerializer


class AboutView(RetrieveAPIView):
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.first()



class LinkView(ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer

class NotificationSubscriptionCreateView(CreateAPIView):

    serializer_class  = NotificationSubscriptionCreateSerializer

    def perform_create(self, serializer):
        ip = get_client_ip(self.request)
        serializer.save(ip_address=ip)


class SettingView(RetrieveAPIView):
    serializer_class = SettingSerializer

    def get_object(self):
        return SiteSetting.objects.first()
class NotificationSubscriptionCountView(GenericAPIView):
    serializer_class = NotificationSubscriptionCountSerializer

    def get(self, request, *args, **kwargs):
        count = NotificationSubscription.objects.count()
        serializer = self.get_serializer({'count': count})
        return Response(serializer.data)


@csrf_exempt
def delete_subscription(request):
    if request.method != "DELETE":
        return HttpResponseBadRequest("Invalid method")

    try:
        data = json.loads(request.body)
        subscription_info = data.get('subscription_info')
        browser_info = data.get('browser_info')
        device_info = data.get('device_info')

        if not (subscription_info and browser_info and device_info):
            return JsonResponse({"error": "Missing parameters"}, status=400)

        subscription = NotificationSubscription.objects.filter(
            subscription_info=subscription_info,
            browser_info=browser_info,
            device_info=device_info
        ).first()

        if not subscription:
            return JsonResponse({"error": "Subscription not found"}, status=404)

        subscription.delete()
        return JsonResponse({"success": "Subscription deleted"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)