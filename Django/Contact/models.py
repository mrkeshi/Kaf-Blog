

# Create your models here.
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="پیغام")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name="تماس"
        verbose_name_plural="تماس ها"