from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/' , Home , name="home"),
    path('login/' , Login , name="login"),\
    path('register/' , Register , name="register"),
    path('forget-password/' , ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , ChangePassword , name="change_password"),
    path('logout/' , Logout , name="logout"),
    
]
