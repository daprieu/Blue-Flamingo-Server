from django.db import models


class Ph(models.Model):
    """Tag Model"""
    ph = models.FloatField()
    message = models.CharField(max_length=175)