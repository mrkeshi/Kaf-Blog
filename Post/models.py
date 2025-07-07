from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان")
    content = RichTextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title