# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-31 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0002_auto_20180331_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='img_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
