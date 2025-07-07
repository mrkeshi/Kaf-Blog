from django.db import models


# Create your models here.
from ckeditor.fields import RichTextField


class About(models.Model):
    title = models.CharField(max_length=150,verbose_name="عنوان صفحه")
    description = RichTextField(verbose_name="توضیحات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تنظیمات درباره من"
        verbose_name_plural = "درباره من"


from django.db import models
from ckeditor.fields import RichTextField


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=150, verbose_name="نام سایت")
    site_url = models.URLField(verbose_name="آدرس سایت", blank=True, null=True)

    site_logo = models.ImageField(upload_to="settings/", verbose_name="لوگو سایت", blank=True, null=True)
    site_icon = models.ImageField(upload_to="settings/", verbose_name="آیکون سایت (favicon)", blank=True, null=True)

    music=models.FileField(upload_to="settings/", verbose_name="موسیقی سایت", blank=True, null=True)

    meta_description = models.CharField(max_length=300, verbose_name="توضیحات سئو", blank=True, null=True)
    meta_keywords = models.CharField(max_length=300, verbose_name="کلمات کلیدی سئو", blank=True, null=True)
    meta_author = models.CharField(max_length=150, verbose_name="نویسنده سئو", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="فعال بودن تنظیمات")

    def __str__(self):
        return self.site_name or "Site Settings"

    class Meta:
        verbose_name = " عمومی"
        verbose_name_plural = " عمومی"

class Links(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    link = models.URLField(verbose_name="لینک")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "لینک های دوستان "
        verbose_name_plural = "لینک های دوستان"