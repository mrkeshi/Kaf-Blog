from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryItemViewSet

router = DefaultRouter()
router.register(r'gallery', GalleryItemViewSet, basename='gallery')

urlpatterns = [
    path('gsllery', include(router.urls)),
]