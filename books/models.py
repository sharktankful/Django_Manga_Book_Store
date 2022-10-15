from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(null=True, max_length=500)
    author = models.CharField(max_length=255)
    editor = models.CharField(max_length=255)
    year_published = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    manga_image = models.ImageField(null=True, blank=True, upload_to='images/')
