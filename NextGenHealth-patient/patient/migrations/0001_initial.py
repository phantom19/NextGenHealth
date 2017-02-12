# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('sex', models.CharField(max_length=1)),
                ('bloodgroup', models.CharField(max_length=3)),
                ('mobile', models.DecimalField(decimal_places=0, max_digits=10)),
                ('house', models.CharField(max_length=25)),
                ('street', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
            ],
        ),
    ]
