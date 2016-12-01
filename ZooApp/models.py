from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as ugtl

from django.db import models
class Species(models.Model):
    kingdom = models.CharField(max_length=25,null=False)
    latin_name = models.CharField(max_length=25)
    common_name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.common_name

class EndangeredSpecies(models.Model):
    species_id = models.OneToOneField(Species,primary_key=True,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.species_id.name

class ExtinctSpecies(models.Model):
    species_id = models.OneToOneField(Species,primary_key=True,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.species_id.name


class Animal(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(max_length=7, choices=(('MALE', 'MALE'), ('FEMALE', 'FEMALE')))
    species_id = models.ForeignKey(Species)

    def __unicode__(self):
        return self.name

class Bird(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(max_length=7,choices=(('MALE','MALE'),('FEMALE','FEMALE')))
    species_id = models.ForeignKey(Species)

    def __unicode__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=25)
    unit_price = models.IntegerField()
    def __unicode__(self):
        return self.name

class AnimalFood(models.Model):
    animal_id = models.ForeignKey(to=Animal,on_delete=models.CASCADE)
    food_id = models.ForeignKey(to = Food,on_delete=models.CASCADE)
    qnty = models.IntegerField()

    class Meta:
        unique_together = (("animal_id","food_id"),)
    def __unicode__(self):
        return self.animal_id.name+"_"+self.food_id.name



class BirdFood(models.Model):
    bird_id = models.ForeignKey(to = Bird,on_delete=models.CASCADE)
    food_id = models.ForeignKey(to = Food,on_delete=models.CASCADE)
    qnty = models.IntegerField()

    class Meta:
        unique_together = (("bird_id","food_id"),)

    def __unicode__(self):
        return self.bird_id.name+"_"+self.food_id.name


"""
class Employee(models.Model):
    fname = models.CharField(max_length=25,null=False)
    lname = models.CharField(max_length=25)
    job_desc = models.CharField(max_length=25, null=False)
    email_id = models.EmailField(max_length=50)
    phone_no = models.CharField(max_length=10)
    Addr = models.CharField(max_length=50)

    def __unicode__(self):
        return self.fname+"_"+self.lname

class AnimalEmp(models.Model):
    animal_id = models.ForeignKey(to=Animal,on_delete=models.CASCADE)
    emp_id = models.ForeignKey(to=Employee,on_delete=models.CASCADE)

class BirdEmp(models.Model):
    bird_id = models.ForeignKey(to=Bird,on_delete=models.CASCADE)
    emp_id = models.ForeignKey(to=Employee,on_delete=models.CASCADE)"""

def validate_positive_finance(val):
    if val < 0:
        raise ValidationError(ugtl("%val is not a positive number"),params={'val':val},)
def validate_phoneno(pno):
    if len(pno) != 10:
        raise ValidationError(ugtl("%pno is not valid"),params={'pno':pno})
class Donor(models.Model):
    name = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=10,validators=[validate_phoneno,])
    mail_id = models.EmailField(max_length=50)
    finance = models.IntegerField(validators=[validate_positive_finance,],default=0)
    addr = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
"""
class AnimalDonor(models.Model):
    animal_id = models.OneToOneField(to=Animal,on_delete=models.CASCADE)
    donor_id = models.ForeignKey(to=Donor,on_delete=models.CASCADE)
    date = models.DateField()
    def __unicode__(self):
        return self.animal_id.name+"_"+self.donor_id.name


class BirdDonor(models.Model):
    bird_id = models.OneToOneField(to=Bird,on_delete=models.CASCADE)
    donor_id = models.ForeignKey(to=Donor,on_delete=models.CASCADE)
    date = models.DateField()

    def __unicode__(self):
        return self.bird_id.name+"_"+self.donor_id.name
"""
class Problem(models.Model):
    desc = models.CharField(max_length=25)
    status = models.CharField(max_length=10,choices=(("solved","solved"),("unsolved","unsolved")))
    def __unicode__(self):
        return self.desc

class AnimalProblem(models.Model):
    animal_id = models.ForeignKey(to=Animal,on_delete=models.CASCADE)
    prob_id = models.ForeignKey(to=Problem,on_delete=models.CASCADE)
    #vetDoctor = models.ForeignKey(to=Employee,null=True,on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.animal_id.name+"_"+self.prob_id.name

class BirdProblem(models.Model):
    bird_id = models.ForeignKey(to=Bird,on_delete=models.CASCADE)
    prob_id = models.ForeignKey(to=Problem,on_delete=models.CASCADE)
    #vetDoctor = models.ForeignKey(to=Employee,null=True,on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.bird_id.name+"_"+self.prob_id.desc





















