# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_auto_20151107_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendedEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=150, null=True, blank=True)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
                ('yes_rsvp_count', models.IntegerField(default=0)),
                ('urlname', models.CharField(max_length=150, null=True, blank=True)),
                ('time', models.DateTimeField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
