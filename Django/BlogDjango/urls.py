"""
URL configuration for BlogDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from rest_framework import permissions

import Post.views
from BlogDjango import settings

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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('Setting.urls')),
    path('api/', include('Contact.urls')),
    path('api/', include('Post.urls')),
    path('api/metadata/', Post.views.HomeSidebarDataView.as_view()),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]

if settings.MODE != 'production':
    urlpatterns += [
        path('api/ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
