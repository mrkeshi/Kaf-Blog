from django.db.models import Count, Q
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Post.models import Tag, Category, Post, Like
from Post.serializers import TagSerializer, CategoryWithPostCountSerializer,PostListSerializer, PostDetailSerializer,LikeCreateSerializer, CommentCreateSerializer


class LatestTagsView(ListAPIView):
    queryset = Tag.objects.order_by('-id')[:50]
    serializer_class = TagSerializer

class CategoryListWithPostCountView(ListAPIView):
    queryset = Category.objects.annotate(post_count=Count('post'))
    serializer_class = CategoryWithPostCountSerializer

class PostListView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(is_draft=False).order_by('-created_at')


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.filter(is_draft=False)
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class LikeCreateView(CreateAPIView):
    serializer_class = LikeCreateSerializer

    def create(self, request, *args, **kwargs):
        ip = request.META.get('REMOTE_ADDR')
        data = request.data.copy()
        data['ip_address'] = ip

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        post = serializer.validated_data['post']
        if Like.objects.filter(post=post, ip_address=ip).exists():
            return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LikeCheckView(APIView):
    def get(self, request, pk):
        ip = request.META.get('REMOTE_ADDR')

        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found'}, status=404)

        liked = Like.objects.filter(post=post, ip_address=ip).exists()
        return Response({'liked': liked})




class CommentCreateView(CreateAPIView):
    serializer_class = CommentCreateSerializer

# جستجوی پست‌ها
class PostSearchView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')  # کوئری رو از پارامتر q بگیر
        return Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            is_draft=False
        ).order_by('-created_at')

# پست‌های یک برچسب خاص
class PostsByTagView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):

        slug = self.kwargs.get('slug')
        return Post.objects.filter(
            tags__slug=slug,
            is_draft=False
        ).order_by('-created_at')


# پست‌های یک دسته‌بندی خاص
class PostsByCategoryView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):

        slug = self.kwargs.get('slug')
        return Post.objects.filter(
            category__slug=slug,
            is_draft=False
        ).order_by('-created_at')