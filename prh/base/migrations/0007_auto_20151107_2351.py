# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20151107_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendedevent',
            name='meetup_id',
            field=models.CharField(default=None, unique=True, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendedevent',
            name='link',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
