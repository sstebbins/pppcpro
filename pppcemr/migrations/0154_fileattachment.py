# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-07 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pppcemr', '0153_remove_treatment_file_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file_attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pppcemr.Treatment')),
            ],
        ),
    ]