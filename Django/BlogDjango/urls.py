from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from rest_framework import permissions
from django.conf import settings
import Post.views

api_base_url = settings.API_BASE_URL

schema_view = get_schema_view(
    openapi.Info(
        title="Kaf API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('sepahan-admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),

    path(f'{api_base_url}', include('Setting.urls')),
    path(f'{api_base_url}', include('Contact.urls')),
    path(f'{api_base_url}', include('Post.urls')),
    path(f'{api_base_url}', include('Gallery.urls')),
    path(f'{api_base_url}metadata/', Post.views.HomeSidebarDataView.as_view()),
]

if settings.MODE != 'production':
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path(f'{api_base_url}ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
