# Generated by Django 2.2.1 on 2019-05-31 10:22

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0005_auto_20190530_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pretrainedmodel',
            name='description',
            field=markdownx.models.MarkdownxField(blank=True, help_text='Enter a brief description of the resource', max_length=1000),
        ),
    ]
