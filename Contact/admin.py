from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from Contact.models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')