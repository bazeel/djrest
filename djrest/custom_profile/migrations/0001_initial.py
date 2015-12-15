# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCustomProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gcm_id', models.CharField(unique=True, max_length=255, verbose_name='GCM ID', blank=True)),
                ('user', models.OneToOneField(related_name='custom_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'custom user profile',
                'verbose_name_plural': 'custom user profile',
            },
        ),
    ]
