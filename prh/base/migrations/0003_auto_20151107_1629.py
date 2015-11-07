# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20151107_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='country_code',
            new_name='country',
        ),
    ]
