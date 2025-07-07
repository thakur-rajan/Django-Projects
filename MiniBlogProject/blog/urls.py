from django.urls import path
from .views import about,contact,dashboard,user_login,user_logout,signup,addPostView,updatePostView,deletePostView

urlpatterns=[
    path('about',about,name='About'),
    path('contact',contact,name='Contact'),
    path('dashboard',dashboard,name='Dashboard'),
    path('login',user_login,name='Login'),
    path('logout',user_logout,name='Logout'),
    path('signup',signup,name='Signup'),
    path('addpost',addPostView,name='AddPost'),
    path('updatepost/<int:id>/',updatePostView,name='UpdatePost'),
    path('deletepost/<int:id>/',deletePostView,name='DeletePost'),
]