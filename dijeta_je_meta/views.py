from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView
from . models import StartUserWeightAndHeight
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request, "dijeta_je_meta/index.html")

@login_required
def userinfo(request):
    info =  StartUserWeightAndHeight.objects.all()
    # info2 = StartUserWeightAndHeight.objects.filter(owner=request.user).last().ime

    context = {'info':info}

    return render(request, "dijeta_je_meta/userinfo.html", context)


  