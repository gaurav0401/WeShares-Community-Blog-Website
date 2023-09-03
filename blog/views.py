from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.

def bloghome(request):
    allpost=models.post.objects.all()
  
    context={'allpost':allpost}
    return render(request , 'blog/bloghome.html' , context)


def blogpost(request , slug):
    userpost=models.post.objects.filter(slug=slug)[0]
    context={'userpost':userpost}


    return render(request , 'blog/blogpost.html' , context)
