from django.contrib import admin

from . import models


@admin.register(models.AdditionalOption)
class AdditionalOptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
