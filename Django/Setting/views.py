from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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