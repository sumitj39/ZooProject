# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalDonor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('animal_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalEmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnty', models.IntegerField()),
                ('animal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='BirdDonor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bird_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Bird')),
            ],
        ),
        migrations.CreateModel(
            name='BirdEmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bird_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Bird')),
            ],
        ),
        migrations.CreateModel(
            name='BirdFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnty', models.IntegerField()),
                ('bird_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Bird')),
            ],
        ),
        migrations.CreateModel(
            name='BirdProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bird_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Bird')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone_no', models.CharField(max_length=10)),
                ('mail_id', models.EmailField(max_length=50)),
                ('addr', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('job_desc', models.CharField(max_length=25)),
                ('email_id', models.EmailField(max_length=50)),
                ('phone_no', models.CharField(max_length=10)),
                ('Addr', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('unit_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=25)),
                ('status', models.CharField(choices=[('solved', 'solved'), ('unsolved', 'unsolved')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom', models.CharField(max_length=25)),
                ('latin_name', models.CharField(max_length=25)),
                ('common_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='EndangeredSpecies',
            fields=[
                ('species_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ZooApp.Species')),
            ],
        ),
        migrations.CreateModel(
            name='ExtinctSpecies',
            fields=[
                ('species_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ZooApp.Species')),
            ],
        ),
        migrations.AddField(
            model_name='birdproblem',
            name='prob_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Problem'),
        ),
        migrations.AddField(
            model_name='birdproblem',
            name='vetDoctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ZooApp.Employee'),
        ),
        migrations.AddField(
            model_name='birdfood',
            name='food_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Food'),
        ),
        migrations.AddField(
            model_name='birdemp',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Employee'),
        ),
        migrations.AddField(
            model_name='birddonor',
            name='donor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Donor'),
        ),
        migrations.AddField(
            model_name='bird',
            name='species_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Species'),
        ),
        migrations.AddField(
            model_name='animalproblem',
            name='prob_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Problem'),
        ),
        migrations.AddField(
            model_name='animalproblem',
            name='vetDoctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ZooApp.Employee'),
        ),
        migrations.AddField(
            model_name='animalfood',
            name='food_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Food'),
        ),
        migrations.AddField(
            model_name='animalemp',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Employee'),
        ),
        migrations.AddField(
            model_name='animaldonor',
            name='donor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Donor'),
        ),
        migrations.AddField(
            model_name='animal',
            name='species_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZooApp.Species'),
        ),
        migrations.AlterUniqueTogether(
            name='birdfood',
            unique_together=set([('bird_id', 'food_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='animalfood',
            unique_together=set([('animal_id', 'food_id')]),
        ),
    ]
