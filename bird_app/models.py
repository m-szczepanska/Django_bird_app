from django.conf import settings
from django.db import models


class Bird(models.Model):
    DISTRIBUTION_CHOICES = (
        ('north', 'north'),
        ('south', 'south'),
        ('west', 'west'),
        ('east', 'east'),
        ('center', 'center')
    )
    HABITAT_CHOICES = (
        ('mountains', 'mountains'),
        ('open plains', 'open plains'),
        ('forests', 'forests'),
        ('rivers and lakes', 'rivers and lakes'),
        ('the seasides', 'the seasides'),
        ('countries and hamlets', 'countries and hamlets'),
        ('urban', 'urban'),
        ('parks and gardens', 'parks and gardens')
    )

    latin_name = models.CharField(max_length=settings.MAX_CHAR_LENGTH)
    eng_name = models.CharField(max_length=settings.MAX_CHAR_LENGTH)
    family = models.CharField(max_length=settings.MAX_CHAR_LENGTH)
    order = models.CharField(max_length=settings.MAX_CHAR_LENGTH)
    distribution = models.CharField(
        max_length=6,
        choices=DISTRIBUTION_CHOICES
    )
    habitat = models.CharField(
        max_length=settings.MAX_CHAR_LENGTH,
        choices=HABITAT_CHOICES
    )


# TODO: add related_name 'photos' to foreign key
class BirdPhoto(models.Model):
    bird = models.ForeignKey('Bird', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=settings.MAX_CHAR_LENGTH)
