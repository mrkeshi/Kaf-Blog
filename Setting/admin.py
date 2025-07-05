# Register your models here.
from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.admin.sites import AdminSite
from Setting.models import About,SiteSetting


@admin.register(About)
class CustomAdminClass(ModelAdmin):
   class Media:
      css = {
         'all': ('/static/css/admin-override.css',)
      }

@admin.register(SiteSetting)
class CustomAdminClass(ModelAdmin):
   pass





