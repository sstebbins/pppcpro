# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-05 01:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pppcemr', '0150_treatmentoption_drug_allergy_cross_reactions'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedTextResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('treatment_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pppcemr.TreatmentOption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
