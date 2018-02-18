# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-18 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Strategy', '0002_auto_20180218_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategy',
            name='files_dir',
            field=models.FileField(choices=[('strategies/bull/normal', '多頭-普通-路徑'), ('strategies/bull/golden', '多頭-黃金-路徑'), ('strategies/bull/platinum', '多頭-白金-路徑'), ('strategies/bull/diamond', '多頭-鑽石-路徑'), ('strategies/bear/normal', '空頭-普通-路徑'), ('strategies/bear/golden', '空頭-黃金-路徑'), ('strategies/bear/platinum', '空頭-白金-路徑'), ('strategies/bear/diamond', '空頭-鑽石-路徑')], null=True, upload_to=''),
        ),
    ]
