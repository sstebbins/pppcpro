# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0116_auto_20160322_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='assessments',
            field=models.ManyToManyField(blank=True, to='pppcemr.Assessment'),
        ),
    ]
