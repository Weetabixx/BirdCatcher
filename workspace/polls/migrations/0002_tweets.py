# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-17 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_profile_picture', models.CharField(max_length=200)),
                ('tweet_hashtag', models.CharField(max_length=200)),
                ('tweet_text', models.CharField(max_length=141)),
                ('tweet_expand_url', models.CharField(max_length=141)),
                ('tweet_image', models.CharField(max_length=200)),
            ],
        ),
    ]
