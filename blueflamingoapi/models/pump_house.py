from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING



class PumpHouse(models.Model):
    """Tag Model"""
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=DO_NOTHING)