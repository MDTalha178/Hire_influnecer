from os import name
from django.urls.conf import path
from django.urls import URLPattern
from . import views

urlpatterns = [
    
    path('hiretuber', views.hiretuber, name="hiretuber"),
   
]