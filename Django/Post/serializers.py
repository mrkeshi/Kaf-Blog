from jalali_date import datetime2jalali
from rest_framework import serializers
from .models import Tag, Category, Post, Comment, Like


def to_jalali_readable2(datetime_obj):
    jalali = datetime2jalali(datetime_obj)

    def to_persian_number(s):
        return str(s).translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹'))

    day = to_persian_number(jalali.day)
    month = jalali.strftime('%B')
    year = to_persian_number(jalali.year)
    time = to_persian_number(datetime_obj.strftime('%H:%M'))

    return f"{day} {month} {year} | {time}"

def to_jalali_readable(dt):
    if not dt:
        return None
    j_date = datetime2jalali(dt)
    return f"{j_date.day} {j_date.strftime('%B %Y')}"



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class CategoryWithPostCountSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'post_count']


class CommentListSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'name', 'message', 'answer', 'created_at']

    def get_created_at(self, obj):
        return to_jalali_readable2(obj.created_at)


class PostListSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    category = CategoryWithPostCountSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'image', 'created_at', 'views',
            'comment_count', 'like_count', 'category', 'tags',
            'is_draft', 'content'
        ]

    def get_created_at(self, obj):
        return to_jalali_readable(obj.created_at)

    def get_comment_count(self, obj):
        return obj.comments.filter(active=True).count()

    def get_like_count(self, obj):
        return obj.likes.count()


class PostDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    category = CategoryWithPostCountSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'image', 'created_at', 'updated_at', 'views',
            'comment_count', 'like_count', 'category', 'tags', 'is_draft',
            'content', 'comments'
        ]

    def get_created_at(self, obj):
        return to_jalali_readable(obj.created_at)

    def get_updated_at(self, obj):
        return to_jalali_readable(obj.updated_at) if obj.updated_at else None

    def get_comments(self, obj):
        qs = obj.comments.filter(active=True)
        return CommentListSerializer(qs, many=True).data

    def get_comment_count(self, obj):
        return obj.comments.filter(active=True).count()

    def get_like_count(self, obj):
        return obj.likes.count()


class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'message']
