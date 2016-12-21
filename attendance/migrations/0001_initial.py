# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-21 06:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.SmallIntegerField(choices=[(0, 'Spring'), (1, 'Fall')])),
                ('year', models.IntegerField()),
                ('class_id', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('password', models.CharField(max_length=16)),
                ('is_open', models.BooleanField(default=True)),
                ('session_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('student_id', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='students_present',
            field=models.ManyToManyField(blank=True, to='attendance.Student'),
        ),
        migrations.AddField(
            model_name='class',
            name='enrolled_students',
            field=models.ManyToManyField(blank=True, to='attendance.Student'),
        ),
    ]
