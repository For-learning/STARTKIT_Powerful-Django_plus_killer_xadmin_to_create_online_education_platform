# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20161103_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='teacher/%Y/%m', verbose_name='\u5934\u50cf'),
        ),
    ]
