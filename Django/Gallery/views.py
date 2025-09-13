# gallery/views.py
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import NotFound
from .models import GalleryItem
from .pagination import DefaultPagination
from .serializers import GalleryItemPublicSerializer, GalleryItemAdminSerializer
from .permissions import IsAdminOrReadCreateOnly

class GalleryItemViewSet(viewsets.ModelViewSet):
    queryset = GalleryItem.objects.all()
    permission_classes = [IsAdminOrReadCreateOnly]
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = DefaultPagination

    def get_serializer_class(self):
        user = getattr(self.request, "user", None)
        if user and user.is_staff:
            return GalleryItemAdminSerializer
        return GalleryItemPublicSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        user = getattr(self.request, "user", None)

        location = self.request.query_params.get("location")
        name = self.request.query_params.get("name")
        status_q = self.request.query_params.get("status")

        if user and user.is_staff and status_q in dict(GalleryItem.Status.choices):
            qs = qs.filter(status=status_q)
        else:
            qs = qs.filter(status=GalleryItem.Status.APPROVED)

        if location:
            qs = qs.filter(location__icontains=location)
        if name:
            qs = qs.filter(sender_name__icontains=name)

        return qs.order_by("-created_at", "-id")

    def get_object(self):
        obj = super().get_object()
        user = getattr(self.request, "user", None)
        if not (user and user.is_staff) and obj.status != GalleryItem.Status.APPROVED:
            raise NotFound()
        return obj
