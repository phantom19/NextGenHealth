# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-08 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_auto_20170108_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medreport',
            name='med_no',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]