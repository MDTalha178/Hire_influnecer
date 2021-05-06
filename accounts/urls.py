from os import name
from django.urls.conf import path
from django.urls import URLPattern
from . import views


urlpatterns = [
    
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_user, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    
]