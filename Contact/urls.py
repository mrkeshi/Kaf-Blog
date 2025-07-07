from Contact.views import ContactMessageCreateView
from django.urls import path
urlpatterns=[
    path('contact', ContactMessageCreateView.as_view(), name='contact'),
]