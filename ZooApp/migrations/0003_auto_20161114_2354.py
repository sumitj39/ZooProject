# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-14 23:54
from __future__ import unicode_literals

import ZooApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZooApp', '0002_donor_finance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='phone_no',
            field=models.CharField(max_length=10, validators=[ZooApp.models.validate_phoneno]),
        ),
    ]
