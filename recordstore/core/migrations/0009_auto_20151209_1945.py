# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151209_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Artist'),
        ),
    ]
