# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190529_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/profile_default.jpg', upload_to='images'),
        ),
    ]
