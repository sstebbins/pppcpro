# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-07 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0151_savedtextresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='file_attachment',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
