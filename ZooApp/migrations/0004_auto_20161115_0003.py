# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-15 00:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZooApp', '0003_auto_20161114_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalemp',
            name='animal_id',
        ),
        migrations.RemoveField(
            model_name='animalemp',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='birdemp',
            name='bird_id',
        ),
        migrations.RemoveField(
            model_name='birdemp',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='animalproblem',
            name='vetDoctor',
        ),
        migrations.RemoveField(
            model_name='birdproblem',
            name='vetDoctor',
        ),
        migrations.DeleteModel(
            name='AnimalEmp',
        ),
        migrations.DeleteModel(
            name='BirdEmp',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
