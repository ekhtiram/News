# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-10 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gridapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Baslik', models.CharField(help_text='Başlık :', max_length=100)),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profil',
            },
        ),
    ]
