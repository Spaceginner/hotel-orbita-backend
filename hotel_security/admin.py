from django.contrib import admin

from . import models


@admin.register(models.Lock)
class LockAdmin(admin.ModelAdmin):
    pass


@admin.register(models.LockGroup)
class LockGroupAdmin(admin.ModelAdmin):
    pass
