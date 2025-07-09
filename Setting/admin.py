# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.sites import AdminSite
from Setting.models import About,SiteSetting,Links,NotificationSubscription


@admin.register(About)
class CustomAdminClass(ModelAdmin):
   pass

@admin.register(SiteSetting)
class CustomAdminClass(ModelAdmin):
   pass

@admin.register(Links)
class CustomAdminClass(ModelAdmin):
   pass

@admin.register(NotificationSubscription)
class CustomAdminClass(ModelAdmin):
   pass




