from django.shortcuts import render,HttpResponseRedirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages
from .forms import SignUpForm,LoginForm,PostForm
from .models import postModel
from django.contrib.auth.models import Group
from django.contrib.auth import  authenticate,login,logout
# from django.contrib.auth.models import User
# Create your views here.

# Home page view
def home(request):
    posts=postModel.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

# About Page view
def about(request):
     return render(request,'blog/about.html')

# Contact page
def contact(request):
    if request.method=='POST':
        fm=ContactForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['fullName']
            email=fm.cleaned_data['email']
            address=fm.cleaned_data['address']
            subject=fm.cleaned_data['subject']
            messages=fm.cleaned_data['message']   
            reg=Contact(fullName=name,email=email,address=address,subject=subject,message=messages) 
            reg.save()
            
            
    else:          
        fm=ContactForm()
    return render(request,'blog/contact.html',{'form':fm}) 

# Dashboard Page view
def dashboard(request):
    if request.user.is_authenticated:  
        posts=postModel.objects.all() 
        user=request.user
        full_name=user.get_full_name()
        grps=user.groups.all()
        
        return render(request,'blog/dashboard.html',{'posts':posts,'fullName':full_name,'groups':grps})
    else:
      return  HttpResponseRedirect('login ')
 
#login view page
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                pwd=fm.cleaned_data['password']
                user=authenticate(username=uname,password=pwd)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login successfully!!!')
                    return HttpResponseRedirect('dashboard')
        else:    
            fm=LoginForm()
        return render(request,'blog/login.html',{'form':fm}) 
    
    else:
        messages.info(request,'You have already logged in')
        return HttpResponseRedirect('dashboard')

#logout view page
def user_logout(request):
    logout(request)
    messages.success(request,'Logged out successfully!!!')
    return HttpResponseRedirect('/')

#Signup view page
def signup(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request,'Congrates ! you became an Author!!')
            return HttpResponseRedirect('dashboard')
    else:
        fm=SignUpForm()                    
    return render(request,'blog/signup.html',{'form':fm})

#Add post view page
def addPostView(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PostForm(request.POST)
            if fm.is_valid():
                title=fm.cleaned_data['title']
                disc=fm.cleaned_data['title']
                reg=postModel(title=title,desc=disc)
                reg.save()
                messages.success(request,'Post Added successfully!!!')
                return HttpResponseRedirect('dashboard')
        else:
            fm=PostForm()    
        return render(request,'blog/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('login')
    
# update post view page
def updatePostView(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=postModel.objects.get(pk=id)
            fm=PostForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Updated Succesfully !!!')
                return HttpResponseRedirect('/blog/dashboard')
        else:
            pi=postModel.objects.get(pk=id)
            fm=PostForm(instance=pi)    
        return render(request,'blog/update.html',{'form':fm})
    else:
        return HttpResponseRedirect('login')
#delete post view page
def deletePostView(request,id:int):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=postModel.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/blog/dashboard') 
    else:
        return HttpResponseRedirect('login')   
