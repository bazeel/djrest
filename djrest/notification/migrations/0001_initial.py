# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 09:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('text', models.TextField(verbose_name='message text')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
                ('users', models.ManyToManyField(blank=True, related_name='notification_lists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'notification list',
                'verbose_name_plural': 'notification lists',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('text', models.TextField(verbose_name='message text')),
                ('success', models.BooleanField(default=False, verbose_name='success')),
                ('response', models.TextField(verbose_name='response from GCM')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='date created')),
                ('date_sent', models.DateField(blank=True, null=True, verbose_name='date created')),
                ('attempt', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='notification.List')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
    ]
