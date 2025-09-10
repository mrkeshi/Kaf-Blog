# gallery_app/models.py
import uuid, os
from io import BytesIO
from django.core.files.base import ContentFile
from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image


def image_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    return f"gallery/{uuid.uuid4()}{ext}"


def validate_image_size(image):
    max_size_mb = 10
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"حداکثر حجم مجاز تصویر {max_size_mb}MB است.")


class GalleryItem(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "در انتظار تایید"
        APPROVED = "approved", "تایید شده"
        REJECTED = "rejected", "رد شده"

    location = models.CharField("لوکیشن", max_length=255)
    sender_name = models.CharField("نام فرستنده", max_length=100)
    sender_email = models.EmailField("ایمیل فرستنده", blank=True, null=True)
    photo = models.ImageField(
        "عکس", upload_to=image_upload_path, validators=[validate_image_size]
    )
    status = models.CharField(
        "وضعیت",
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        db_index=True,
    )
    created_at = models.DateTimeField("زمان ایجاد", auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            img = Image.open(self.photo.path)
            new_width = img.width // 2
            new_height = img.height // 2
            img = img.resize((new_width, new_height), Image.LANCZOS)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            buffer = BytesIO()
            img.save(buffer, format="JPEG", quality=75, optimize=True)

            file_name = os.path.basename(self.photo.name)
            self.photo.save(file_name, ContentFile(buffer.getvalue()), save=False)

            buffer.close()
            super().save(update_fields=["photo"])

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "آیتم گالری"
        verbose_name_plural = "آیتم‌های گالری"

    def __str__(self):
        return f"{self.sender_name} - {self.location} ({self.status})"
