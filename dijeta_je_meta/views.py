from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView
from . models import StartUserWeightAndHeight

# Create your views here.
def home_view(request):
    return render(request, "dijeta_je_meta/index.html")

class UserInfo(ListView):
    model = StartUserWeightAndHeight
    template_name = "dijeta_je_meta/userinfo.html"


  