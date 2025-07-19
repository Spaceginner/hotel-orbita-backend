from django.contrib import admin

from . import models


@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SeasonSale)
class SeasonSaleAdmin(admin.ModelAdmin):
    pass
