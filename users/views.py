from django.shortcuts import render
from . forms import SignUpForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

class Signup(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("userinfo")











