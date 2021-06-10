from django.db import models


class FilterPressure(models.Model):
    """Tag Model"""
    psi = models.IntegerField()
    message = models.CharField(max_length=175)