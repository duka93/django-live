from email.policy import default
from random import choices
from tkinter.tix import Tree
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django import forms


# Create your models here.

class StartUserWeightAndHeight(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ime = models.CharField(max_length=25, default="")
    pocetna_tezina = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(400),
            MinValueValidator(60)
        ]
    )
    visina = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(250),
            MinValueValidator(140)
        ]
    )

    moderate = "Umeren"
    aggressive = "Agresivan"
    diet_pace_choices = [
        (moderate, "Umeren"),
        (aggressive, "Agresivan")
    ]
    stepen_gubitka_tezine = models.CharField(max_length=20, choices=diet_pace_choices, default=moderate)

    pol_m = "Muški"
    pol_z = "Ženski"

    polovi = [
        (pol_m,"Muški"),
        (pol_z,"Ženski")
    ]
    pol = models.CharField(max_length=6, choices=polovi,default=pol_m)

    
    def __str__(self):
        return self.ime + " - Pocetna tezina i visina"


class CurrentWeight(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    trenutna_tezina = models.IntegerField()
    detalji = models.TextField(blank=True)
