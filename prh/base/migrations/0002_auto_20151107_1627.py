# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='access_token',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='expires_in',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='refresh_token',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='token_type',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
