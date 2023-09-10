from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
     path('', views.home , name="home"),
     path('about', views.about , name="about"),
     path('contact', views.contact , name="contact"),
     path('search', views.search , name="search"),
     path('signup', views.handleSignUp , name="signup"),
     path('login', views.handlelogin , name="login"),
     path('logout', views.handlelogout , name="signup"),
     path('createblog', views.createblog , name="createblog"),

]
