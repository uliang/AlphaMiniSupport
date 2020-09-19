from django.shortcuts import render, reverse
from django.contrib.auth import views as auth_views

# Create your views here.


class LoginView(auth_views.LoginView) : 
    template_name = 'account/login.html'

class LogoutView(auth_views.LogoutView) : 
    next_page = '/'