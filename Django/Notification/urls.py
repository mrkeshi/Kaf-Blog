from django.urls import path
from . import views

urlpatterns = [
    path('notifications/',            views.notification_list,        name='notification-list'),
    path('notifications/mark-read/',  views.mark_notifications_read,  name='notification-mark-read'),
]
