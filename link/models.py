from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.urls import reverse
from django import forms
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver



CATALOG_CHOICES = [
    ('code', 'Code'),
    ('news', 'News'),
    ('shopping', 'Shopping'),
    ('sport', 'Sport'),
    ('games', 'Games'),
    ('videos', 'Videos'),
    ('music', 'Music'),
    ('work', 'Work'),
]


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    catalogChoice = MultiSelectField(choices=CATALOG_CHOICES, default='code',  max_choices=5, min_choices=1,)
    REQUIRED_FIELDS = ['catalogChoice']


class LinkDB(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    url = models.URLField(max_length=200, blank=True)
    isPrivate = models.BooleanField(default=False)
    catalogChoice = models.CharField(choices=CATALOG_CHOICES, default='code', max_length=20)
