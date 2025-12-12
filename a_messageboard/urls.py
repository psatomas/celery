from django.urls import path
from .views import messageboard_view, subscribe

urlpatterns = [
    path('', messageboard_view, name='messageboard'),
    path('subscribe/', subscribe, name='subscribe'),
]
