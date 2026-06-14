from django.contrib import admin
from .models import Notification, NotificationRead


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display  = ['title', 'type', 'is_active', 'created_at']
    list_filter   = ['type', 'is_active']
    search_fields = ['title', 'message']
    list_editable = ['is_active']
    ordering      = ['-created_at']


@admin.register(NotificationRead)
class NotificationReadAdmin(admin.ModelAdmin):
    list_display  = ['notification', 'client_token', 'read_at']
    list_filter   = ['notification']
    search_fields = ['client_token']
    readonly_fields = ['read_at']
