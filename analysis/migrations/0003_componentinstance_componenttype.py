# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20180524_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentinstance',
            name='componentType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.VisComponent'),
        ),
    ]
