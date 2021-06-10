from django.db import models


class Ph(models.Model):
    """Tag Model"""
    ph = models.IntegerField()
    message = models.CharField(max_length=175)