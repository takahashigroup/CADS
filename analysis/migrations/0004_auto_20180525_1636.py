# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 07:36
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_componentinstance_componenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentinstance',
            name='contents',
            field=jsonfield.fields.JSONField(),
        ),
    ]
