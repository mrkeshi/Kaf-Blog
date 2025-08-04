from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import re

def strip_html_and_send(self):
    plain_text = re.sub('<[^<]+?>', '', self.content)  # حذف تگ‌ها
    send_push_to_all(self.title, plain_text[:100], self.slug)


from Post.utils import send_push_to_all


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام دسته‌بندی")
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, verbose_name="اسلاگ")
    meta_description = models.CharField(max_length=200, default=" ")
    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


# --- برچسب ---
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name="نام برچسب")
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, verbose_name="اسلاگ")
    meta_description = models.CharField(max_length=200,default=" ")
    class Meta:
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب‌ها"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


# --- پست ---
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    content = RichTextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='post_images',null=True, blank=True,verbose_name= "تصویر")
    created_at = models.DateTimeField(verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    is_draft = models.BooleanField(default=False, verbose_name="پیش‌نویس")
    views = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدید")
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True, verbose_name="اسلاگ")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته‌بندی")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="برچسب‌ها")
    send_notification = models.BooleanField(default=False, verbose_name="ارسال نوتیفیکیشن")
    seo_keywords = models.CharField(max_length=100, default=" ",verbose_name= "کلمات کلیدی")
    seo_description = models.CharField(max_length=200, default=" ", verbose_name="توضیحات سئو")
    author = models.ForeignKey('auth.User', blank=True,null=True,on_delete=models.CASCADE, verbose_name="نویسنده")
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست‌ها"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

        super().save(*args, **kwargs)

        if self.send_notification:
            send_push_to_all(self.title, self.seo_description,self.slug)
            self.send_notification = False
            super().save(update_fields=['send_notification'])

    def get_absolute_url(self):
        return f"/posts/{self.slug}/"

    def like_count(self):
        return self.likes.count()

    def comment_count(self):
        return self.comments.count()


# --- دیدگاه ---
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="پست")
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="متن دیدگاه")
    answer = RichTextField(verbose_name="پاسخ دیدگاه" , blank=True)
    active=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    privte=models.BooleanField(default=False, verbose_name=" نظرخصوصی ")
    class Meta:
        verbose_name = "دیدگاه"
        verbose_name_plural = "دیدگاه‌ها"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.post.title}"


# --- لایک ---
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', verbose_name="پست")
    ip_address = models.GenericIPAddressField(verbose_name="آی‌پی کاربر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ لایک")

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک‌ها"
        unique_together = ('post', 'ip_address')
        indexes = [
            models.Index(fields=['post', 'ip_address']),
        ]
    def __str__(self):
        return f"{self.ip_address} -> {self.post.title}"
