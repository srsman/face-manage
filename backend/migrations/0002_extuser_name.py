# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='\u59d3\u540d'),
        ),
    ]