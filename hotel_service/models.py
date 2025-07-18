from django.db import models

from hotel_finances.models import Price


class MealPlan(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=True)
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)


class Service(models.Model):
    name = models.CharField(blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=True)
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)


class AdditionalOption(models.Model):
    name = models.CharField(blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=True)
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)
