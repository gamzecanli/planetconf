from django.db import models


class Planet(models.Model):
    planet_name = models.CharField(max_length=64)
    link = models.CharField(max_length=128)
    planet_directory_name = models.CharField(max_length=64)


class Blogger(models.Model):
    blogger_name = models.CharField(max_length=64)
    blogger_link = models.CharField(max_length=256)
