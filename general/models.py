from django.db import models
import string
from random import choice


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=False)
    password_hash = models.CharField(max_length=200, blank=False)
    session = models.CharField(max_length=200, blank=True)
    salt = models.CharField(max_length=200, blank=False)


POLL_TYPES =(
    # ('A_SC', 'Anonymous, single choice'),
    ('A_MC', 'Anonymous, multiple choice'),
    # ('N_SC', 'Not anonymous, single choice'),
    ('N_MC', 'Not anonymous, multiple choice')
)

PIS_TYPE =(
    ('M', 'Мen'),
    ('W', 'Women'),
)


class Poll(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500, blank=True)
    variants = models.CharField(max_length=2000, blank=False)
    votes = models.CharField(max_length=100, blank=False)
    author = models.ForeignKey('User', on_delete=models.CASCADE, blank=False, default=None)
    type = models.CharField(max_length=4, choices=POLL_TYPES, blank=False)


class Vote(models.Model):
    user_id = models.CharField(max_length=200, blank=False)
    poll_id = models.CharField(max_length=200, blank=False)
    selected_options = models.CharField(max_length=200, blank=False)