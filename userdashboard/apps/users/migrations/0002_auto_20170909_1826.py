# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-10 01:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]