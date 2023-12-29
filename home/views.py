from django.shortcuts import render , redirect
from django.http import HttpResponse 
from home.models import Contact
from django.contrib.auth.models import User

from datetime import datetime

from django.contrib import messages 

from blog import models

from django.contrib.auth import logout, authenticate, login

from blog.views import bloghome

from  blog.forms import PostForm

# Create your views here.

def home(request):
     allpost=models.post.objects.all().order_by('-date')[:3]
  
     context={'allpost':allpost}

     return render(request , 'home/home.html' , context)

def about(request):
    return render(request , 'home/about.html')

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




def search(request):
    query=request.GET['query']
    if len(query)==0:
        messages.error(request , "No such  results are found.")
        allpost=[]
    elif len(query)>70 :
        messages.warning(request , "Your query is too long. Please refine your query.")
        allpost=[]
    else:
        allposttitle=models.post.objects.filter(title__icontains=query)
        allpostcontent=models.post.objects.filter(content__icontains=query)
        allpost=allposttitle.union(allpostcontent)
    params={'allpost':allpost}
    return render(request, 'home/search.html' , params)


def handleSignUp(request):
    if request.method=='POST':
         username=request.POST['username']
         fname=request.POST['fname']
         lname=request.POST['lname']
         email=request.POST['email']
         pass1=request.POST['pass1']
         pass2=request.POST['pass2']

         if (len(username) >10 ):
             messages.warning(request,"username must be under 10 character  ")
             return redirect('home')
      
         
         if pass1!=pass2:
             messages.warning(request, "Password didn't matched , try again....")
             return redirect('home')

         else:

         #create user
           try:
             myuser=User.objects.create_user(username , email , pass1)
             myuser.first_name=fname
             myuser.last_name=lname
             myuser.save()
             messages.success(request , "Your account has been created successfully....")
             return redirect('home')
           except:
               messages.error(request , "User already exist")
               return redirect('home')

    else:
        return HttpResponse("404- Not allowed")
    

def handlelogin(request):
    if request.method == "POST":
      user=request.POST['loginusername']
      passwd=request.POST['loginPassword']
      user=authenticate(username=user , password=passwd)
      if user is not None:
         login(request, user)
         messages.success(request , f"Welcome back  {request.user.get_full_name()}")
         return  redirect('home')
      else:
         messages.error(request , "Incorrect username or password.....try again")
         return redirect('home')
    return HttpResponse("404- Not Found")

def handlelogout(request):
    logout(request)
    messages.success(request , f"You have been successfully logged out")
    return redirect('home')



def createblog(request):
    form = PostForm
    context = {
        'form':form
        }
    return render(request , 'home/create.html' , context)
    
