# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-01 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZooApp', '0004_auto_20161115_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animaldonor',
            name='animal_id',
        ),
        migrations.RemoveField(
            model_name='animaldonor',
            name='donor_id',
        ),
        migrations.RemoveField(
            model_name='birddonor',
            name='bird_id',
        ),
        migrations.RemoveField(
            model_name='birddonor',
            name='donor_id',
        ),
        migrations.DeleteModel(
            name='AnimalDonor',
        ),
        migrations.DeleteModel(
            name='BirdDonor',
        ),
    ]