from django.db import models


class FreeChlorine(models.Model):
    """Tag Model"""
    ppm = models.IntegerField()
    message = models.CharField(max_length=175)