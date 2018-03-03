# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 07:53
from __future__ import unicode_literals

import Strategy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Strategy', '0007_auto_20180225_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strategy',
            name='avg_return',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='平均報酬率'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='category',
            field=models.CharField(choices=[('bull', '多頭'), ('bear', '空頭')], max_length=255, verbose_name='多空頭類別'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='上傳日期'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='description',
            field=models.TextField(verbose_name='策略敘述'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='files_dir',
            field=models.FileField(upload_to=Strategy.models.file_path, verbose_name='檔案上傳'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='level',
            field=models.CharField(choices=[('normal', '普通'), ('golden', '黃金'), ('platinum', '白金'), ('diamond', '鑽石')], max_length=255, verbose_name='會員等級'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='like',
            field=models.PositiveIntegerField(default=0, verbose_name='喜歡數'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='max_loss',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='最大虧損率'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='max_return',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='最高報酬率'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='修改日期'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='name',
            field=models.CharField(max_length=255, verbose_name='策略名稱'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='standard',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='標準差'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='total_return',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='總報酬率'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='total_transa',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='總交易次數'),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='win_percent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='勝率'),
        ),
    ]
