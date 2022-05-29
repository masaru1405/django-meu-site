from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationFormWithEmail

#4h30m
class SignUpView(generic.CreateView):
   form_class = UserCreationFormWithEmail
   success_url = reverse_lazy('login')
   template_name = 'accounts/signup.html'
