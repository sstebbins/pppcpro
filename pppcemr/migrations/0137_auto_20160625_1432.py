# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-25 18:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0136_remove_treatmentoption_cpt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cptcode',
            options={'verbose_name_plural': 'CPT code'},
        ),
    ]