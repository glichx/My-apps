from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

# Create your views here.
# class LoginPageView(TemplateView):
#     success_url = reverse_lazy("home")
#     template_name = 'registration/login.html'

# class SignupPageView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = 'registration/signup.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class User_InfoPageView(TemplateView):
    template_name = 'user_info.html'
    