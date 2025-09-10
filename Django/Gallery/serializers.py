from rest_framework import serializers
from .models import GalleryItem

class GalleryItemPublicSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)

    class Meta:
        model = GalleryItem
        fields = ["id", "location", "sender_name", "sender_email", "photo", "status", "created_at"]
        read_only_fields = ["id", "status", "created_at"]

    def validate_sender_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("نام فرستنده باید حداقل ۲ کاراکتر باشد.")
        return value

class GalleryItemAdminSerializer(GalleryItemPublicSerializer):
    status = serializers.ChoiceField(choices=GalleryItem.Status.choices, required=False)
