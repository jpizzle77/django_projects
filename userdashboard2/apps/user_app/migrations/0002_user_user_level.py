# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-22 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.CharField(default='Guest', max_length=10),
        ),
    ]
