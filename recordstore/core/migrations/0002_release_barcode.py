# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='barcode',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
