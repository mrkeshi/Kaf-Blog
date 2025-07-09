import pytz
from django.contrib import admin
from django.utils.html import format_html
from jalali_date import date2jalali, datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date.widgets import AdminSplitJalaliDateTime, AdminJalaliDateWidget

from .forms import PostAdminForm
from .models import Category, Tag, Post, Comment, Like


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Post)
class PostAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    form = PostAdminForm

    list_display = ('title', 'category', 'is_draft', 'views', 'created_at_jalali', 'updated_at_jalali')
    list_filter = ('category', 'is_draft')
    search_fields = ('title', 'content', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)

    def created_at_jalali(self, obj):
        if obj.created_at:
            return jalali_converter(obj.created_at)
        return "-"
    created_at_jalali.short_description = 'تاریخ ایجاد (جلالی)'

    def updated_at_jalali(self, obj):
        if obj.updated_at:
            return jalali_converter(obj.updated_at)
        return "-"
    updated_at_jalali.short_description = 'تاریخ بروزرسانی (جلالی)'



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'email', 'created_at_jalali')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

    def created_at_jalali(self, obj):
        if obj.created_at:
            return jalali_converter(obj.created_at)
        return "-"
    created_at_jalali.short_description = 'تاریخ ثبت (جلالی)'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'ip_address', 'created_at_jalali')
    search_fields = ('ip_address', 'post__title')

    def created_at_jalali(self, obj):
        if obj.created_at:
            return jalali_converter(obj.created_at)
        return "-"
    created_at_jalali.short_description = 'تاریخ لایک (جلالی)'
