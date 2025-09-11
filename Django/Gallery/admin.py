from django.contrib import admin

from Post.admin import jalali_converter
from .models import GalleryItem

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("id", "sender_name", "location", "sender_email", "status", "created_at_jalali")
    list_filter = ("status", "created_at")
    search_fields = ("sender_name", "location", "sender_email")
    list_editable = ("status",)

    actions = ["approve_items", "reject_items"]
    def created_at_jalali(self, obj):
        if obj.created_at:
            return jalali_converter(obj.created_at)
        return "-"
    created_at_jalali.short_description = 'تاریخ ایجاد (جلالی)'

    @admin.action(description="تایید آیتم‌های انتخاب‌شده")
    def approve_items(self, request, queryset):
        queryset.update(status=GalleryItem.Status.APPROVED)

    @admin.action(description="رد آیتم‌های انتخاب‌شده")
    def reject_items(self, request, queryset):
        queryset.update(status=GalleryItem.Status.REJECTED)
