from django.urls import path,include
from .views import AboutView, SettingView, LinkView, NotificationSubscriptionCreateView, \
    NotificationSubscriptionCountView, delete_subscription

urlpatterns=[
path('about/',AboutView.as_view(),name='about'),
path('setting/',SettingView.as_view(),name='setting'),
path('links/',LinkView.as_view(),name='links'),
    path('notification-subscriptions/', NotificationSubscriptionCreateView.as_view(),
         name='notification-subscription-create'),
    path('notification-subscriptions/count/', NotificationSubscriptionCountView.as_view(),
         name='notification-subscription-count'),
    path('notification-subscriptions/unsubscribe/', delete_subscription, name='delete_subscription'),

]