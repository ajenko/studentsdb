# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20170724_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='students_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0430'),
        ),
    ]
