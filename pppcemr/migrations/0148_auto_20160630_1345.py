# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-30 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0147_auto_20160630_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='workplan',
            name='max_age_months',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workplan',
            name='min_age_months',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
