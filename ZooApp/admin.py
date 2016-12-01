from django.contrib import admin
from ZooApp.models import Species
from ZooApp import models

# Register your models here.
iters = [models.Species,models.Animal,models.AnimalFood,
         models.AnimalProblem,models.Bird,models.BirdFood,
         models.BirdProblem,models.Food,models.Problem,models.ExtinctSpecies,
         models.EndangeredSpecies,models.Donor]

admin.site.register(iters)
admin.site.site_header= "Wildlife Administration"
#admin.site.site_title = "Wildlife Administration"
#admin.site.index_title = "Sumit"
