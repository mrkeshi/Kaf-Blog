# gallery_app/models.py
import os
import uuid
from io import BytesIO

from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import models

from PIL import Image, ImageOps


def image_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1].lower()
    return f"gallery/{uuid.uuid4()}{ext}"


def validate_image_size(image):
    max_size_mb = 15
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"حداکثر حجم مجاز تصویر {max_size_mb}MB است.")


class GalleryItem(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "در انتظار تایید"
        APPROVED = "approved", "تایید شده"
        REJECTED = "rejected", "رد شده"

    location = models.CharField("لوکیشن", max_length=255)
    sender_name = models.CharField("نام فرستنده", max_length=100)
    photo = models.ImageField("عکس", upload_to=image_upload_path, validators=[validate_image_size])
    status = models.CharField(
        "وضعیت",
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        db_index=True,
    )
    created_at = models.DateTimeField("زمان ایجاد", auto_now_add=True)

    MAX_SIDE = 2560

    def _should_downscale(self, width: int, height: int) -> bool:
        return max(width, height) > self.MAX_SIDE

    def _save_image_safely(self, pil_img: Image.Image, original_ext: str) -> ContentFile:
        fmt = (pil_img.format or "").upper()
        ext = original_ext.lower()
        buf = BytesIO()

        if not fmt:
            if ext in [".jpg", ".jpeg"]:
                fmt = "JPEG"
            elif ext == ".png":
                fmt = "PNG"
            elif ext == ".webp":
                fmt = "WEBP"
            elif ext == ".gif":
                fmt = "GIF"
            elif ext == ".bmp":
                fmt = "BMP"
            else:
                fmt = None

        save_kwargs = {}

        will_be_jpeg = fmt == "JPEG" or ext in (".jpg", ".jpeg")
        if will_be_jpeg and pil_img.mode in ("RGBA", "LA", "P"):
            background = Image.new("RGB", pil_img.size, (255, 255, 255))
            if pil_img.mode in ("RGBA", "LA"):
                background.paste(pil_img, mask=pil_img.split()[-1])
            else:
                background.paste(pil_img)
            pil_img = background
        elif pil_img.mode == "P" and fmt != "GIF":
            pil_img = pil_img.convert("RGBA")

        if fmt == "JPEG":
            save_kwargs.update(dict(format="JPEG", quality=82, optimize=True, progressive=True, subsampling=0))
        elif fmt == "PNG":
            save_kwargs.update(dict(format="PNG", optimize=True, compress_level=6))
        elif fmt == "WEBP":
            lossless = bool(pil_img.info.get("lossless", False))
            if lossless:
                save_kwargs.update(dict(format="WEBP", lossless=True, quality=100, method=6))
            else:
                save_kwargs.update(dict(format="WEBP", quality=92, method=6))
        elif fmt in ("GIF", "BMP"):
            save_kwargs.update(dict(format=fmt))
        else:
            if ext in (".jpg", ".jpeg"):
                save_kwargs.update(dict(format="JPEG", quality=92, optimize=True, progressive=True, subsampling=0))
            elif ext == ".png":
                save_kwargs.update(dict(format="PNG", optimize=True, compress_level=6))
            elif ext == ".webp":
                save_kwargs.update(dict(format="WEBP", quality=92, method=6))
            else:
                save_kwargs.update(dict(format=fmt or "PNG"))

        pil_img.save(buf, **save_kwargs)
        buf.seek(0)
        return ContentFile(buf.getvalue())

    def save(self, *args, **kwargs):
        old_path = None
        if self.pk:
            try:
                old = type(self).objects.only("photo").get(pk=self.pk)
                old_path = old.photo.name or None
            except type(self).DoesNotExist:
                old_path = None

        super().save(*args, **kwargs)

        if not self.photo:
            return

        current_path = self.photo.name

        self.photo.open("rb")
        original_bytes = self.photo.read()
        self.photo.close()

        img_file = BytesIO(original_bytes)
        with Image.open(img_file) as im:
            original_ext = os.path.splitext(current_path)[1]
            orig_w, orig_h = im.width, im.height

            im_fixed = ImageOps.exif_transpose(im)

            changed = False
            if self._should_downscale(orig_w, orig_h):
                im_fixed.thumbnail((self.MAX_SIDE, self.MAX_SIDE), Image.LANCZOS)
                changed = True

            if im_fixed.size != (orig_w, orig_h) or changed:
                content = self._save_image_safely(im_fixed, original_ext)
                default_storage.delete(current_path)
                self.photo.save(current_path, content, save=False)
                super().save(update_fields=["photo"])

        if old_path and old_path != current_path:
            default_storage.delete(old_path)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "آیتم گالری"
        verbose_name_plural = "آیتم‌های گالری"

    def __str__(self):
        return f"{self.sender_name} - {self.location} ({self.status})"
