# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]