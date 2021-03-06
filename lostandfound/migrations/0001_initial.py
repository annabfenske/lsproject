# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('net_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Net ID')),
                ('n_number', models.CharField(max_length=10, verbose_name='N#')),
                ('first_name', models.CharField(max_length=250, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=250, verbose_name='Last Name')),
                ('nyu_email', models.EmailField(max_length=254)),
                ('id_lost', models.BooleanField(default=False)),
            ],
        ),
    ]
