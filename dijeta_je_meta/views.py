from calendar import week
from multiprocessing import context
from re import A
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from . models import StartUserWeightAndHeight, CurrentWeight
from django.contrib.auth.decorators import login_required
from . forms import AddCurrentWeight, CreateInfoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.utils import formats
import datetime
import calendar
import math

# Create your views here.
def home_view(request):
    return render(request, "dijeta_je_meta/index.html")


# Za dobijanje proseka od 7 prethodnih fiksnih tezina
def week_avg(request):
    counter = 6
    counter2 = 0

    while len(CurrentWeight.objects.filter(owner=request.user)) > counter:  
        c = CurrentWeight.objects.filter(owner=request.user).order_by('date_added')[counter2:counter+1]
        counter += 7
        counter2 += 7
        week_avg = 0

        for i in range(7): # Sa for loopom ides kroz elemente liste koju si iznad napravio u query-ju!
            week_avg += c[i].trenutna_tezina
        week_avg = round(week_avg/7,2)
    return week_avg

# Za izracunavanje idealne tezine
def ideal_weight(request):
    if StartUserWeightAndHeight.objects.filter(owner=request.user):
        if StartUserWeightAndHeight.objects.filter(owner=request.user).first().pol == "Мuški":
           ideal_kg = 50+(0.91*(StartUserWeightAndHeight.objects.filter(owner=request.user).first().visina-152.4))
        else:
            ideal_kg = 50+(0.91*(StartUserWeightAndHeight.objects.filter(owner=request.user).first().visina-152.4))
        return ideal_kg

# Za izracunavanje razlike izmedju idealne i trenutne tezine
def weight_diff(ideal,current):
    if current > ideal:
        avg_loss_per_week = current*0.01
        razlika_kg = current-ideal

        today = datetime.datetime.today()
        end_date = today

        while (current > ideal):
          end_date = end_date + datetime.timedelta(days = 7)
          current -= avg_loss_per_week

        razlika = f"Treba da izgubite jos {razlika_kg} kg, idealan datum bi bio {datetime.datetime.strftime(end_date, '%d-%b-%Y')}"
        return razlika


@login_required
def userinfo(request):
    #Inicijalni set podataka
    info =  request.user.startuserweightandheight_set.all()
    context ={'info':info}

    # Nakon unosenja inicijalnog seta podataka
    if StartUserWeightAndHeight.objects.filter(owner=request.user):
        trenutna_tezina = StartUserWeightAndHeight.objects.filter(owner=request.user).first().pocetna_tezina
        context['trenutna_tezina'] = trenutna_tezina
        idealna_tezina = round(ideal_weight(request))
        context['idealna_tezina'] = idealna_tezina
        razlika_kg = weight_diff(idealna_tezina, StartUserWeightAndHeight.objects.filter(owner=request.user).first().pocetna_tezina)
        context['razlika_kg'] = razlika_kg
        bmi = round(StartUserWeightAndHeight.objects.filter(owner=request.user).first().pocetna_tezina / pow(StartUserWeightAndHeight.objects.filter(owner=request.user).first().visina/100,2),1)
        context['bmi'] = bmi

    # Nakon prvog unosa trenutne tezine
    if len(CurrentWeight.objects.filter(owner=request.user)) > 0:
       trenutna_tezina = CurrentWeight.objects.filter(owner=request.user).first().trenutna_tezina
       poslednji_unos = CurrentWeight.objects.filter(owner=request.user).first().date_added
       context['trenutna_tezina'] = trenutna_tezina
       context['poslednji_unos']=poslednji_unos
    
    # Nakon 7 unosa trenutne tezine
    if len(CurrentWeight.objects.filter(owner=request.user)) > 6:   
        week = week_avg(request)
        razlika_kg = weight_diff(idealna_tezina,week)
        bmi = round(week / pow(StartUserWeightAndHeight.objects.filter(owner=request.user).first().visina/100,2),1)
        context['razlika_kg'] = razlika_kg
        context['bmi'] = bmi
        context['week_avg'] = week

    return render(request, "dijeta_je_meta/userinfo.html", context)


@login_required
def history(request):
    counter = 6
    counter2 = 0
    list = []
    list2 = []
    list3 = []
    context={}

    while len(CurrentWeight.objects.filter(owner=request.user)) > counter:  
        c = CurrentWeight.objects.filter(owner=request.user).order_by('date_added')[counter2:counter+1]
        counter += 7
        counter2 += 7
        week_avg = 0
        for i in range(7):
            week_avg += c[i].trenutna_tezina
        week_avg = round(week_avg/7,2)

        list.append(week_avg)
        date_start_pull = c[1].date_added
        date_start = datetime.datetime.strftime(date_start_pull, '%d-%b-%Y')

        list2.append(date_start)
        date_end_pull = c[6].date_added
        date_end = datetime.datetime.strftime(date_end_pull, '%d-%b-%Y')
        list3.append(date_end)
        lists = zip(list,list2,list3)

        context['lists'] = lists
    return render(request, "dijeta_je_meta/history.html", context)


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
    template_name = "dijeta_je_meta/current_weight.html"
    success_url = reverse_lazy("userinfo")
    def form_valid(self, form): # Sa ovim oznacavmo da se instanca nove pice se pridodaje trenutnom useru
       form.instance.owner = self.request.user
       return super().form_valid(form)


class ListCurrentWeight(LoginRequiredMixin,ListView):
    model = CurrentWeight
    template_name = "dijeta_je_meta/weight_list.html"

    def get_queryset(self): #sa ovim querijem cemo vratiti samo objekte koji pripadaju trenutnom useru
        return CurrentWeight.objects.filter(owner=self.request.user)