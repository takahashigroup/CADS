# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 07:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0003_pretrainedmodel_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pretrainedmodel',
            name='componentInstance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.ComponentInstance'),
        ),
        migrations.AlterField(
            model_name='pretrainedmodel',
            name='metadata',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
