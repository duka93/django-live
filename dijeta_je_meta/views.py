from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from . models import StartUserWeightAndHeight, CurrentWeight
from django.contrib.auth.decorators import login_required
from . forms import AddCurrentWeight, CreateInfoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

# Create your views here.
def home_view(request):
    return render(request, "dijeta_je_meta/index.html")

@login_required
def userinfo(request):
    info =  request.user.startuserweightandheight_set.all()
    if len(CurrentWeight.objects.filter(owner=request.user)) > 0:
       trenutna_tezina=CurrentWeight.objects.filter(owner=request.user).last().trenutna_tezina
       poslednji_unos=CurrentWeight.objects.filter(owner=request.user).last().date_added
       context = {'info':info,"trenutna_tezina":trenutna_tezina,"poslednji_unos":poslednji_unos}
    else:
        context = {'info':info}
    # info2 = StartUserWeightAndHeight.objects.filter(owner=request.user).last().ime OVO KADA BUDES TRAZIO IZ SVOG MODELA VREDNOSTI

    # owner = StartUserWeightAndHeight.objects.get("owner")
    # if owner.owner != request.user:
    #     raise Http404
    return render(request, "dijeta_je_meta/userinfo.html", context)


class CreateInfo(LoginRequiredMixin,CreateView):
    model = StartUserWeightAndHeight
    form_class = CreateInfoForm
    template_name = "dijeta_je_meta/createinfo.html"
    success_url = reverse_lazy("userinfo")
    def form_valid(self, form): # Sa ovim oznacavmo da se instanca nove pice se pridodaje trenutnom useru
       form.instance.owner = self.request.user
       return super().form_valid(form)

 



class AddCurrentWeight(LoginRequiredMixin,CreateView):
    model = CurrentWeight
    form_class = AddCurrentWeight
    template_name="dijeta_je_meta/current_weight.html"
    success_url = reverse_lazy("userinfo")
    def form_valid(self, form): # Sa ovim oznacavmo da se instanca nove pice se pridodaje trenutnom useru
       form.instance.owner = self.request.user
       return super().form_valid(form)



class ListCurrentWeight(LoginRequiredMixin,ListView):
    model = CurrentWeight
    template_name="dijeta_je_meta/weight_list.html"
    def get_queryset(self): #sa ovim querijem cemo vratiti samo objekte koji pripadaju trenutnom useru
        return CurrentWeight.objects.filter(owner=self.request.user)