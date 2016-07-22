# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-01 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0148_auto_20160630_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='allergic_reaction_symptoms',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatmentoption',
            name='type',
            field=models.CharField(choices=[('NT', 'Note'), ('LB', 'Lab'), ('IL', 'In House Lab'), ('VI', 'Vital Signs'), ('RX', 'Drug Prescription'), ('PR', 'Procedure'), ('TS', 'Test'), ('HP', 'HPI and ROS'), ('PE', 'Physical Exam'), ('PF', 'PFSH'), ('FU', 'Follow-up Instructions'), ('VA', 'Vaccine / Immunization'), ('AL', 'Drug Allergy')], default='NT', max_length=2),
        ),
    ]