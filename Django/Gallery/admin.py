import pytz
from django.contrib import admin
from jalali_date import date2jalali
def jalali_converter(datetime_obj):
    local_time = datetime_obj.astimezone(pytz.timezone('Asia/Tehran'))
    jalali_date = date2jalali(local_time)
    months = [
        "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
        "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
    ]
    year = jalali_date.year
    month_name = months[jalali_date.month - 1]
    day = jalali_date.day
    hour = local_time.hour
    minute = local_time.minute
    return f"{day} {month_name} {year} - {hour:02d}:{minute:02d}"

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
