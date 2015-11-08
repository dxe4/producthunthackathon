from django.db import models
from django_pgjson.fields import JsonField
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    joined = models.DateTimeField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    other_services = JsonField(null=True, blank=True)
    # auth data
    expires_in = models.DateTimeField(null=True, blank=True)
    access_token = models.CharField(max_length=255)
    token_type = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)


class AttendedEvent(models.Model):
    user = models.ForeignKey(User)
    link = models.CharField(max_length=150, null=True, blank=True)
    meetup_id = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    yes_rsvp_count = models.IntegerField(default=0)
    urlname = models.CharField(max_length=150, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
