from django.urls import path
from a_home.views import home_view

urlpatterns = [
    path('', home_view, name="home"),  
]
