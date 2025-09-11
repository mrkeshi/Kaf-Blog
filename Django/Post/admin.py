from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from .forms import PostAdminForm
from .models import Category, Tag, Post, Comment, Like
from .utils import jalali_converter


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
