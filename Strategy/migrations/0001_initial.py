# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-18 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='s_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='s_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('standard', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('avg_return', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_return', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('max_return', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_transa', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('max_loss', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('win_percent', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('files_dir', models.FileField(null=True, upload_to=(('strategies/bull/normal', '多頭-普通-路徑'), ('strategies/bull/golden', '多頭-黃金-路徑'), ('strategies/bull/platinum', '多頭-白金-路徑'), ('strategies/bull/diamond', '多頭-鑽石-路徑'), ('strategies/bear/normal', '空頭-普通-路徑'), ('strategies/bear/golden', '空頭-黃金-路徑'), ('strategies/bear/platinum', '空頭-白金-路徑'), ('strategies/bear/diamond', '空頭-鑽石-路徑')))),
                ('like', models.PositiveIntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Strategy.s_category')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Strategy.s_level')),
            ],
        ),
    ]