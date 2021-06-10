from django.db import models


class CyanuricAcid(models.Model):
    """Tag Model"""
    ppm = models.IntegerField()
    message = models.CharField(max_length=175)