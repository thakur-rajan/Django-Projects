from django.urls import path
from .views import deleteData,updateData,userRagistrationView,user_login,profileView,user_logout,changePassword,changePassword2
urlpatterns=[
    path('delete/<int:id>/',deleteData,name='deleteData'),
    path('update/<int:id>/',updateData,name='updateData'),
    path('signup/',userRagistrationView,name='SignUp'),
    path('login/',user_login,name='Login'),
    path('logout/',user_logout,name='Logout'),
    path('profile/',profileView,name='Profile'),
    path('passwordChange/',changePassword,name='PasswordChange'),
    path('passwordchange2/',changePassword2,name='PasswordChange2'),
  
    
]