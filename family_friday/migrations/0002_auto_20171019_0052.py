# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family_friday', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
