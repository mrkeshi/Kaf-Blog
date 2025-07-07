import pytz
from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from jalali_date import date2jalali
from Contact.models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at_jalali')

    def created_at_jalali(self, obj):
        # تبدیل به زمان منطقه تهران
        local_time = obj.created_at.astimezone(pytz.timezone('Asia/Tehran'))
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

    created_at_jalali.short_description = 'تاریخ ایجاد (جلالی)'