from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .form import Registration,signUp,EditUserData,EditAdminData
from .models import Student
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Add and Show Function
def home(request):
    if request.method=='POST':
        fm=Registration(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name'] 
            dob=fm.cleaned_data['dob']
            address=fm.cleaned_data['address']  
            phoneNumber=fm.cleaned_data['phoneNumber'] 
            email=fm.cleaned_data['email']         
            gender=fm.cleaned_data['gender'] 
            course=fm.cleaned_data['course'] 
            reg=Student(
                name=name,dob=dob,address=address,
                phoneNumber=phoneNumber,email=email,gender=gender,
                course=course
                )
            reg.save() 
            messages.success(request,'✅Added Successful!!!')
        print("Form Errors:", fm.errors.as_data())
             
     
    else:    
        fm=Registration()
    stu=Student.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'student':stu})
# Delete Function
def deleteData(request,id):
    if request.method=='POST':
        data=Student.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')
    else:
        messages.error(request,'Data din\'t Deleted')
         

# Update Function
def updateData(request, id):
    if request.method=='POST':
        data=Student.objects.get(pk=id)
        fm=Registration(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
            messages.success(request,'✅ Updated Successfull !!!')
        else:
            messages.error(request,'Form is not validated')    

    else:
        studentData=Student.objects.get(pk=id)
        fm=Registration(instance=studentData)     
    return  render(request,'enroll/update.html',{'form':fm})  

# User Registration 
def userRagistrationView(request):
    if request.method == 'POST':
        fm= signUp(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'✅ User Created successfully !!!')
            # print("Form Errors:", fm.errors.as_data())
            return HttpResponseRedirect('/enroll/login/')
    
    else:
        fm=signUp()
    return render(request,'enroll/signup.html',{'form':fm})

# Login 
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request,data=request.POST)
            if fm.is_valid():
                print('99999999999999999999') 
                uname=fm.cleaned_data['username']
                upas=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upas)
                
                if user is not None:
                    login(request,user)   
                    return HttpResponseRedirect('/enroll/profile/')
                    # messages.success(request,'✅ Login Successfully!!!')
                else:
                    messages.error(request,'Invalid Username or Password')    
            else:
                messages.error(request,'Invalid Credential')        
        else:
            fm=AuthenticationForm()            
        return render(request,'enroll/login.html',{'form':fm})
    else:
        return render(request,'enroll/profile.html',{'name':request.user})
        
#logout
def user_logout(request):
    logout(request)   
    messages.success(request,'you have successfully log out')       
    return HttpResponseRedirect('/enroll/login/') 

# profile View function
def profileView(request):
   if request.user.is_authenticated: 
       
     if request.method=='POST':
         if request.user.is_superuser:
             fm=EditAdminData(instance=request.user,data=request.POST)
             if fm.is_valid():
                 fm.save()
                 messages.success(request,'Updated successfully!!')
         else:        
            fm=EditUserData(instance=request.user,data=request.POST) 
            if fm.is_valid():
                fm.save()
                messages.success(request,'Updated successfully !!')      
     else: 
         if request.user.is_superuser:
             fm=EditAdminData(instance=request.user)
         else:    
             fm=EditUserData(instance=request.user)
     return render(request,'enroll/profile.html',{'name':request.user,'form':fm}) 
   else:
       return HttpResponseRedirect('/enroll/login/') 
# change password with old password
def changePassword(request):

    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                # messages.success(request,'Password changed sucessfully !!')
                return HttpResponseRedirect('/enroll/login/')
        else:
            fm=PasswordChangeForm(request.user)
        return render(request,'enroll/changepassword.html',{'form':fm})
    else:
      return  HttpResponseRedirect('/enroll/login/')
#change password without old password
def changePassword2(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SetPasswordForm(request.user,data=request.POST)
            if fm.is_valid():
                user=fm.save()
                update_session_auth_hash(request,user)
                messages.success(request,'Password Update Successfully!!')
                return   HttpResponseRedirect('/enroll/login/')
        else:
            fm=SetPasswordForm(request.user)
        return render(request,'enroll/changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect('/enroll/login/')  
          
  
            
