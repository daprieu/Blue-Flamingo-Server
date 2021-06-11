from django.db import models


class Token(models.Model):
    user = models.OneToOneField("Technician", on_delete=models.CASCADE)
    created = models.CharField(max_length=50)