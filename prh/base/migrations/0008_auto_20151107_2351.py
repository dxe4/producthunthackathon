# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20151107_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendedevent',
            name='meetup_id',
            field=models.CharField(max_length=20, unique=True, null=True, blank=True),
        ),
    ]
