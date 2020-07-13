# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-24 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentinstance',
            name='accessibility',
            field=models.CharField(choices=[('pri', 'Private'), ('int', 'Internal'), ('pub', 'Public')], default='pri', max_length=3),
        ),
        migrations.AddField(
            model_name='componentinstance',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a brief description of the resource', max_length=1000),
        ),
        migrations.AddField(
            model_name='componentinstance',
            name='shared_groups',
            field=models.ManyToManyField(blank=True, related_name='ci_shared_groups', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='componentinstance',
            name='shared_users',
            field=models.ManyToManyField(blank=True, related_name='ci_shared_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='viscomponent',
            name='accessibility',
            field=models.CharField(choices=[('pri', 'Private'), ('int', 'Internal'), ('pub', 'Public')], default='pri', max_length=3),
        ),
        migrations.AddField(
            model_name='viscomponent',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a brief description of the resource', max_length=1000),
        ),
        migrations.AddField(
            model_name='viscomponent',
            name='shared_groups',
            field=models.ManyToManyField(blank=True, related_name='viscomponent_shared_groups', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='viscomponent',
            name='shared_users',
            field=models.ManyToManyField(blank=True, related_name='viscomponent_shared_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workspace',
            name='accessibility',
            field=models.CharField(choices=[('pri', 'Private'), ('int', 'Internal'), ('pub', 'Public')], default='pri', max_length=3),
        ),
        migrations.AddField(
            model_name='workspace',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a brief description of the resource', max_length=1000),
        ),
        migrations.AddField(
            model_name='workspace',
            name='shared_groups',
            field=models.ManyToManyField(blank=True, related_name='workspace_shared_groups', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='workspace',
            name='shared_users',
            field=models.ManyToManyField(blank=True, related_name='workspace_shared_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='componentinstance',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique ID for this particular resource', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='componentinstance',
            name='name',
            field=models.CharField(help_text='Enter the name of the resource', max_length=200),
        ),
        migrations.AlterField(
            model_name='viscomponent',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique ID for this particular resource', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='viscomponent',
            name='name',
            field=models.CharField(help_text='Enter the name of the resource', max_length=200),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='Unique ID for this particular resource', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='name',
            field=models.CharField(help_text='Enter the name of the resource', max_length=200),
        ),
    ]
