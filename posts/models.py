from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')


