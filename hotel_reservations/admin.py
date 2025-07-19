from django.contrib import admin

from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ReservationPackage)
class ReservationPackageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RoomReservation)
class RoomReservationAdmin(admin.ModelAdmin):
    pass
