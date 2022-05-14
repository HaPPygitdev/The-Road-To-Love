from django.db import models

POLL_TYPES = (
    # ('A_SC', 'Anonymous, single choice'),
    ('A_MC', 'Anonymous, multiple choice'),
    # ('N_SC', 'Not anonymous, single choice'),
    ('N_MC', 'Not anonymous, multiple choice')
)

PIS_TYPE = (
    ('Men', 'Мen'),
    ('Women', 'Women'),
)


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=False)
    password_hash = models.CharField(max_length=200, blank=False)
    first_name = models.CharField(max_length=100, blank=True)
    second_name = models.CharField(max_length=100, blank=True)
    age = models.CharField(max_length=3, blank=True)
    gender = models.CharField(max_length=10, choices=PIS_TYPE, blank=True)
    session = models.CharField(max_length=200, blank=True)
    salt = models.CharField(max_length=200, blank=False)


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


PLACE_TYPES = (
    ('cafe', 'Cafe'),
    ('cinema', 'Cinema')
)


class Posts(models.Model):
    title = models.CharField('Название', max_length=50)
    place = models.CharField('Place', max_length=10, choices=PLACE_TYPES, blank=True, default='cafe')
    full_text = models.TextField('Статья', max_length=500)
    author_p = models.ForeignKey('User', on_delete=models.CASCADE, blank=False, default=None)


class Temporary(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=200, blank=True)
    confirm_password = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    second_name = models.CharField(max_length=100, blank=True)
    age = models.CharField(max_length=3, blank=True)
    gender = models.CharField(max_length=10, choices=PIS_TYPE, blank=True)
    session = models.CharField(max_length=200, blank=True)
    salt = models.CharField(max_length=200, blank=False)