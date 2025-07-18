from django.db import models
from django.db.models import CheckConstraint, Q

from hotel.models import Hotel


class Price(models.Model):
    class Meta:
        constraints = [
            CheckConstraint(
                name='fixed_or_relative',
                check=Q(fixed__isnull=False) ^ Q(relative__isnull=False)
            )
        ]

    fixed = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    relative = models.DecimalField(max_digits=6, decimal_places=3, null=True)


class SeasonSale(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='season_sales', related_query_name='season_sale', on_delete=models.CASCADE, null=False)
    discount = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)
