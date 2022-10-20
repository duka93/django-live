from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from . models import StartUserWeightAndHeight
from django.contrib.auth.decorators import login_required
from . forms import Createinfoform
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

# Create your views here.
def home_view(request):
    return render(request, "dijeta_je_meta/index.html")

@login_required
def userinfo(request):
    info =  request.user.startuserweightandheight_set.all()
    # info2 = StartUserWeightAndHeight.objects.filter(owner=request.user).last().ime OVO KADA BUDES TRAZIO IZ SVOG MODELA VREDNOSTI
    context = {'info':info}
    # owner = StartUserWeightAndHeight.objects.get("owner")
    # if owner.owner != request.user:
    #     raise Http404
    return render(request, "dijeta_je_meta/userinfo.html", context)


class CreateInfo(LoginRequiredMixin,CreateView):
    model = StartUserWeightAndHeight
    form_class = Createinfoform
    template_name = "dijeta_je_meta/createinfo.html"
    success_url = reverse_lazy("userinfo")
    def form_valid(self, form): # Sa ovim oznacavmo da se instanca nove pice se pridodaje trenutnom useru
       form.instance.owner = self.request.user
       return super().form_valid(form)


  