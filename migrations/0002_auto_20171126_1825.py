# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autotriage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyserver',
            name='added_by',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='companyserver',
            name='deleted',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, default='pic_folder/None/default.jpg', null=True, upload_to='profiles/'),
        ),
    ]