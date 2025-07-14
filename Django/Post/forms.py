from django import forms
from jalali_date.widgets import AdminSplitJalaliDateTime
from .models import Post

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'created_at': AdminSplitJalaliDateTime,
            'updated_at': AdminSplitJalaliDateTime,
        }
