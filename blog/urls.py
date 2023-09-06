from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
        #API's 
    path('deleteblog/<int:sno>' , views.deleteblog , name='deleteblog'),
    path('postblog' , views.postblog , name='postblog'),
    path('contact' , views.contact , name='contact'),
    path('postcomment' , views.postComment , name='postcomment'),
    path('', views.bloghome , name="bloghome"),

    path('<str:slug>', views.blogpost , name="blogpost"),

    
]


