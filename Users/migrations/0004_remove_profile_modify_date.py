# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-17 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20180217_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='modify_date',
        ),
    ]