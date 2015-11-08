# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_attendedevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendedevent',
            name='link',
            field=models.CharField(max_length=150, unique=True, null=True, blank=True),
        ),
    ]
