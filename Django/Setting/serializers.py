from rest_framework import serializers

from Setting.models import About,SiteSetting,Links,NotificationSubscription


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = '__all__'
class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'

class NotificationSubscriptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSubscription
        fields = ['subscription_info', 'ip_address', 'browser_info', 'device_info']

class NotificationSubscriptionCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()