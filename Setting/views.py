from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView

from Setting.models import About, SiteSetting,Links
from Setting.serializers import AboutSerializer, SettingSerializer,LinksSerializer


class AboutView(RetrieveAPIView):
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.first()

class SettingView(RetrieveAPIView):
    serializer_class = SettingSerializer

    def get_object(self):
        return SiteSetting.objects.first()

class LinkView(ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer