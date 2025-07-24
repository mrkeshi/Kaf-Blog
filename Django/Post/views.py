from django.db.models import Count, Q
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from Post.models import Tag, Category, Post, Like
from Post.serializers import TagSerializer, CategoryWithPostCountSerializer,PostListSerializer, PostDetailSerializer,LikeCreateSerializer, CommentCreateSerializer
from Setting.models import Links
from Setting.serializers import LinksSerializer
from .utils import get_client_ip


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


from django.db.models import F
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostDetailSerializer

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.filter(is_draft=False)
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        Post.objects.filter(pk=instance.pk).update(views=F('views') + 1)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# class LikeCreateView(CreateAPIView):
#     serializer_class = LikeCreateSerializer
#
#     def create(self, request, *args, **kwargs):
#
#         data = request.data.copy()
#
#         ip= get_client_ip(request)
#         data['ip_address'] =ip
#
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#
#         post = serializer.validated_data['post']
#         if Like.objects.filter(post=post, ip_address=ip).exists():
#             return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
#
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
class LikeCreateView(APIView):
    def post(self, request, *args, **kwargs):
        post_id = request.data.get("post")
        if not post_id:
            return Response({"code": 0, "detail": "post ID is required"}, status=HTTP_400_BAD_REQUEST)

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"code": 0, "detail": "Post not found"}, status=HTTP_400_BAD_REQUEST)

        ip = get_client_ip(request)
        existing_like = Like.objects.filter(post=post, ip_address=ip).first()

        if existing_like:
            existing_like.delete()
            return Response({
                "code": 2,
                "status": "disliked",
                "post": post_id
            }, status=HTTP_200_OK)

        # Otherwise, create the like
        serializer = LikeCreateSerializer(data={"post": post_id})
        if serializer.is_valid():
            serializer.save(ip_address=ip)
            return Response({
                "code": 1,
                "status": "liked",
                "post": post_id
            }, status=HTTP_200_OK)
        else:
            return Response({"code": 0, "detail": serializer.errors}, status=HTTP_400_BAD_REQUEST)

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


class HomeSidebarDataView(APIView):
    def get(self, request, *args, **kwargs):
        tags = Tag.objects.order_by('-id')[:50]
        categories = Category.objects.annotate(post_count=Count('post'))
        links = Links.objects.all()

        tag_serializer = TagSerializer(tags, many=True)
        category_serializer = CategoryWithPostCountSerializer(categories, many=True)
        link_serializer = LinksSerializer(links, many=True)

        return Response({
            'tags': tag_serializer.data,
            'categories': category_serializer.data,
            'links': link_serializer.data
        }, status=status.HTTP_200_OK)