from django.urls import path,include
from .views import AboutView,SettingView,LinkView
urlpatterns=[
path('about',AboutView.as_view(),name='about'),
path('setting',SettingView.as_view(),name='setting'),
path('links',LinkView.as_view(),name='links'),

]