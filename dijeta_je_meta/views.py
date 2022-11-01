from os import link
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import StartUserWeightAndHeight, CurrentWeight
from django.contrib.auth.decorators import login_required
from . forms import AddCurrentWeight, CreateInfoForm, UpdateStartWeightAndHeight, UpdateWeightForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import datetime
from django.contrib import messages

# Create your views here.
def home_view(request):
    return render(request, "dijeta_je_meta/index.html")

def instructions_view(request):
    return render(request, "dijeta_je_meta/instructions.html")

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

        razlika = f"Ukupno treba da izgubite jos: {round(razlika_kg,1)} kg"
        avg_loss_per_week = f"U toku narednih 7 unosa treba da izgubite: {round(avg_loss_per_week,1)} kg"
        end_day = f"Idealan datum završetka dijete: {datetime.datetime.strftime(end_date, '%d-%b-%Y')}"
        return (razlika, avg_loss_per_week, end_day)

    elif current == ideal:
        razlika = f"Čestitamo, postigli ste željenu kilažu!"
        avg_loss_per_week = f"U toku narednih 7 unosa treba da izgubite: 0 kg"
        end_day = f"Idealan datum završetka dijete: Samo održavajte trenutnu kilažu :) "
        return (razlika, avg_loss_per_week, end_day)
    
    else:
        avg_gain_per_week = current*0.01
        razlika_kg = ideal-current

        today = datetime.datetime.today()
        end_date = today

        while (current < ideal):
          end_date = end_date + datetime.timedelta(days = 7)
          current += avg_gain_per_week

        razlika = f"Ukupno treba da se ugojite jos: {razlika_kg} kg"
        avg_gain_per_week = f"U toku narednih 7 unosa treba da dobijete: {round(avg_gain_per_week,1)} kg"
        end_day = f"Idealan datum završetka dijete: {datetime.datetime.strftime(end_date, '%d-%b-%Y')}"
        return (razlika, avg_gain_per_week, end_day)

#Za izracunavanje kalorija, proteina itd.
def calculate_macros(ideal,current):
     if current > ideal:
        protein = round((2.2*current)*0.7)
        calories = round((current*2.2)*13 - ((current*2.2*13)*25/100))
        fat = round(calories*25/100/9)
        carbs = round((calories - (protein*4 + fat*9))/4)
        return (protein, calories, fat, carbs)

     if current < ideal:
        protein = round((2.2*current)*0.7)
        calories = round((current*2.2)*13 + ((current*2.2*13)*25/100))
        fat = round(calories*25/100/9)
        carbs = round((calories - (protein*4 + fat*9))/4)
        return (protein, calories, fat, carbs)

     else:
        protein = round((2.2*current)*0.7)
        calories = round((current*2.2)*13)
        fat = round(calories*25/100/9)
        carbs = round((calories - (protein*4 + fat*9))/4)
        return (protein, calories, fat, carbs)

@login_required
def userinfo(request):
    
    #Inicijalni set podataka
    info =  request.user.startuserweightandheight_set.all()
    context ={'info':info}

    # Nakon unosenja inicijalnog seta podataka
    if StartUserWeightAndHeight.objects.filter(owner=request.user):
        trenutna_tezina = StartUserWeightAndHeight.objects.filter(owner=request.user).first().pocetna_tezina
        idealna_tezina = round(ideal_weight(request))
        razlika_kg = weight_diff(idealna_tezina, trenutna_tezina)
        (razlika, prosek, kraj) = razlika_kg 
        bmi = round(StartUserWeightAndHeight.objects.filter(owner=request.user).first().pocetna_tezina / pow(StartUserWeightAndHeight.objects.filter(owner=request.user).first().visina/100,2),1)
        macros = calculate_macros(idealna_tezina,trenutna_tezina)
        (proteini, kalorije, masti, carbs) = macros
        
        context['carbs'] = carbs
        context['masti'] = masti
        context['proteini'] = proteini
        context['kalorije'] = kalorije
        context['razlika'] = razlika
        context['prosek'] = prosek
        context['kraj'] = kraj
        context['trenutna_tezina'] = trenutna_tezina
        context['idealna_tezina'] = idealna_tezina
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
        (razlika, prosek, kraj) = razlika_kg 
        bmi = round(week / pow(StartUserWeightAndHeight.objects.filter(owner=request.user).first().visina/100,2),1)
        macros = calculate_macros(idealna_tezina,week)
        (proteini, kalorije, masti, carbs) = macros
        
        context['carbs'] = carbs
        context['masti'] = masti
        context['proteini'] = proteini
        context['kalorije'] = kalorije
        context['razlika'] = razlika
        context['prosek'] = prosek
        context['kraj'] = kraj
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
    list4 = []
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
        list4.append(f"{round(ideal_weight(request)-week_avg,2)}")
        lists = zip(list,list2,list3,list4)

        context['lists'] = lists
    return render(request, "dijeta_je_meta/history.html", context)


class CreateInfo(LoginRequiredMixin,CreateView):
    model = StartUserWeightAndHeight
    form_class = CreateInfoForm
    template_name = "dijeta_je_meta/createinfo.html"
    success_url = reverse_lazy("instructions")
    def form_valid(self, form): # Sa ovim oznacavmo da se instanca nove pice se pridodaje trenutnom useru
       form.instance.owner = self.request.user
       messages.success(self.request, 'Čestitamo, uspešno ste kreirali nalog!')
       return super().form_valid(form)

 
class AddCurrentWeight(LoginRequiredMixin,CreateView):
    model = CurrentWeight
    form_class = AddCurrentWeight
    template_name = "dijeta_je_meta/current_weight.html"
    success_url = reverse_lazy("userinfo")
    def form_valid(self, form): # Sa ovim oznacavmo da se instanca nove pice se pridodaje trenutnom useru
       form.instance.owner = self.request.user
       messages.add_message(self.request, messages.SUCCESS, 'Uspešno ste dodali novu tezinu!')
       return super().form_valid(form)


class ListCurrentWeight(LoginRequiredMixin,ListView):
    model = CurrentWeight
    template_name = "dijeta_je_meta/weight_list.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ListCurrentWeight, self).get_context_data(*args,**kwargs)
        return context

    def get_queryset(self): #sa ovim querijem cemo vratiti samo objekte koji pripadaju trenutnom useru
        return CurrentWeight.objects.filter(owner=self.request.user)


class UpdateStartWeightAndHeight(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = StartUserWeightAndHeight
    template_name = "dijeta_je_meta/update_info.html"
    form_class = UpdateStartWeightAndHeight

    def test_func(self):
        start_user = self.get_object()
        if self.request.user != start_user.owner:
            return False
        else:
            return True


class UpdateCurrentWeight(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CurrentWeight
    template_name="dijeta_je_meta/update_weight.html"
    form_class = UpdateWeightForm
    
    def test_func(self):
        cw = self.get_object()
        if self.request.user != cw.owner:
            return False
        else:
            return True

class DeleteCurrentWeight(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CurrentWeight
    template_name = "dijeta_je_meta/delete_weight.html"
    success_url = reverse_lazy("weightlist")
     
    def test_func(self):
        cw = self.get_object()

        if self.request.user == cw.owner:
            return True
        return False







