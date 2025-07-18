from django.contrib import admin

from . import models


@admin.register(models.Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass
