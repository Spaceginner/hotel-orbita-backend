from django.db import models

from hotel_finances.models import Price


class MealPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class AdditionalOption(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    price = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.name}"
