from django.shortcuts import render , redirect
from django.http import HttpResponse 
from blog.models import post , handleComments 
from home.models import Contact
from datetime import datetime
from blog.templatetags import get_dict
from . import models
from django.contrib import messages 


# Create your views here.

def bloghome(request):
    allpost=models.post.objects.all()
  
    context={'allpost':allpost}


    return render(request , 'blog/bloghome.html' , context)

def blog(request ):
    allpost=models.post.objects.all()
  
    context={'allpost':allpost}

    return render(request , 'blog/bloghome.html' , context)


def blogpost(request , slug):
    userpost=models.post.objects.filter(slug=slug).first()
    userpost.views+=1
    userpost.save()
    comments=models.handleComments.objects.filter(post=userpost , parent=None)
    replies=models.handleComments.objects.filter(post=userpost).exclude(parent=None)
    total=models.handleComments.objects.filter(post=userpost).count()
    repdict={}
    for reply in replies:
        if reply.parent.sno not in repdict.keys():
            repdict[reply.parent.sno]= [reply]
        else:
            repdict[reply.parent.sno].append(reply)
    context={'userpost':userpost , 'comments': comments , 'total':total , 'repdict':repdict }


    return render(request , 'blog/blogpost.html' , context )


def postComment(request):
    if request.user.is_authenticated:
      if request.method=='POST' :
        comment= request.POST['comment']
        user = request.user
        postsno = request.POST['postsno']
        parentsno = request.POST['parentsno']
        post=models.post.objects.get(sno=postsno)
      
        if (len(comment)==0):
            messages.error(request, "Empty comments can't be posted.")
        else:
         if parentsno=="":
            comment=models.handleComments(comment=comment , user=user , post=post)
         else:
             parent=models.handleComments.objects.get(sno=parentsno)
             comment=models.handleComments(comment=comment , user=user , post=post , parent=parent)
         comment.save()
         messages.success(request , f"Your Comment has been recorded...")
         return redirect(f'/blog/{post.slug}' )
    else:
        messages.warning(request , f"Login first to make comment on the article.")
        return redirect('/blog/')

    return redirect(f'/blog/' )


def postblog(request):
    if request.method == 'POST' and request.user.is_authenticated:
         title=request.POST['title']
         content=request.POST['content']
         author=request.POST['author']
         category=request.POST['Category']
         
         date=datetime.now()
         user = request.user

         if (len(title)==0 or len(content)==0 or len(author)==0):
            messages.error(request , "Please fill all the  fields properly before saving blog. ")
         else:
            post=models.post(title=title, content=content , author=author, date=date , category=category , user=user)
            post.save()
            messages.success(request , f"Your Blog has been published successfully...")
            return redirect(f'/blog/{post.slug}')
    else:
        messages.warning(request, "Please Login first to publish your article.")
    return redirect('/')



def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        if (len(name)<2 or len(email)<2  ):
            messages.error(request , "Please, first fill details before submitting")
        else:
            contact=Contact(name=name , email=email, phone=phone , desc=desc , date=datetime.now())
            contact.save()
            messages.success(request, "Your response has been recorded, We will contact you soon.... ")

    return render(request , 'home/contact.html')

def deleteblog(request , sno):
    if request.user.is_authenticated:
        post=models.post.objects.get(sno=sno)
     
        post.delete()
        print(sno)
        messages.success(request, "Article has been deleted successfully")

    else:

        messages.error(request, "Permission denied, Only admin of this blog can modify this article.")
    
    return redirect('/')
