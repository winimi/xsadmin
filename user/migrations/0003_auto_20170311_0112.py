# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20170310_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='traffic_rate',
            field=models.PositiveIntegerField(default=100, help_text='100表示默认1倍', verbose_name='流量倍率百分比'),
        ),
    ]
