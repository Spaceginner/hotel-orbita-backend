from django.contrib import admin

from . import models


@admin.register(models.Building)
class BuildingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Floor)
class FloorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RoomCategory)
class RoomCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RoomFeature)
class RoomFeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RoomUnavailability)
class RoomUnavailabilityAdmin(admin.ModelAdmin):
    pass
