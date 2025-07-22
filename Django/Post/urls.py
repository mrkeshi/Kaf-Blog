from django.urls import path
from .views import LatestTagsView, CategoryListWithPostCountView, PostListView, PostDetailView, LikeCreateView, \
    LikeCheckView, CommentCreateView, PostSearchView, PostsByTagView, PostsByCategoryView

urlpatterns = [
    path('tags/', LatestTagsView.as_view(), name='latest-tags'),
    path('categories/', CategoryListWithPostCountView.as_view(), name='category-list-with-count'),

    # --- Post related (مهم: اول خاص‌ها، بعد عمومی)
    path('posts/search/', PostSearchView.as_view(), name='post-search'),
    path('posts/tag/<str:slug>/', PostsByTagView.as_view(), name='posts-by-tag'),
    path('posts/category/<str:slug>/', PostsByCategoryView.as_view(), name='posts-by-category'),
    path('posts/<str:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),

    # --- Like & Comment
    path('likes/create/', LikeCreateView.as_view(), name='like-create'),
    path('likes/check/<int:pk>/', LikeCheckView.as_view(), name='like-check'),
    path('comments/create', CommentCreateView.as_view(), name='comment-create'),

]