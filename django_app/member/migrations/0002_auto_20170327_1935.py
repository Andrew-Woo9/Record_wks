# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='author',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
