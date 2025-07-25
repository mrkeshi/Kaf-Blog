from rest_framework import serializers

from Setting.models import About,SiteSetting,Links,NotificationSubscription


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
class SettingSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = SiteSetting
        exclude = ['id']

    def get_count(self, obj):
        from .models import NotificationSubscription
        return NotificationSubscription.objects.count()

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'


class NotificationSubscriptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSubscription
        fields = ['subscription_info', 'browser_info', 'device_info']

class NotificationSubscriptionCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()