from django.contrib.auth.models import User
from django.db import models

class PumphouseParameters(models.Model):
    date = models.DateTimeField()
    pumphouse = models.ForeignKey("PumpHouse", on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    hardness = models.ForeignKey("Hardness", on_delete=models.SET_NULL, blank=True, null=True)
    hardness_note = models.CharField(max_length=175)
    total_chlorine = models.ForeignKey("TotalChlorine", on_delete=models.SET_NULL, blank=True, null=True)
    free_chlorine = models.ForeignKey("FreeChlorine", on_delete=models.SET_NULL, blank=True, null=True)
    chlorine_note = models.CharField(max_length=175)
    ph = models.ForeignKey("Ph", on_delete=models.SET_NULL, blank=True, null=True)
    ph_note = models.CharField(max_length=175)
    alkalinity = models.ForeignKey("Alkalinity", on_delete=models.SET_NULL, blank=True, null=True)
    alkalinity_note = models.CharField(max_length=175)
    cyanuric_acid = models.ForeignKey("CyanuricAcid", on_delete=models.SET_NULL, blank=True, null=True)
    cyanuric_acid_note = models.CharField(max_length=175)
    salinity = models.ForeignKey("Salinity", on_delete=models.SET_NULL, blank=True, null=True)
    salinity_note = models.CharField(max_length=175)
    filter_pressure = models.ForeignKey("FilterPressure", on_delete=models.SET_NULL, blank=True, null=True)
    filter_pressure_note = models.CharField(max_length=175)
    filter_basket = models.BooleanField()