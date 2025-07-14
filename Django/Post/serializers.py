from rest_framework import serializers
from .models import Tag,Category,Post

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']
class CategoryWithPostCountSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'post_count']

from rest_framework import serializers
from .models import Post, Comment, Like

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'message', 'answer', 'created_at']


class PostListSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    category = CategoryWithPostCountSerializer()
    tags = TagSerializer()
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'image', 'created_at', 'views',
            'comment_count', 'like_count', 'category', 'tags',
            'is_draft', 'content'
        ]

    def get_comment_count(self, obj):
        return obj.comments.filter(active=True).count()

    def get_like_count(self, obj):
        return obj.likes.count()


class PostDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

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
        fields = ['post', 'ip_address']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'message']
