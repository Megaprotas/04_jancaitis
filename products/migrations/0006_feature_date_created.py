# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_feature_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
