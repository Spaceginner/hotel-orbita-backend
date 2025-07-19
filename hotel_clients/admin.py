from django.contrib import admin

from . import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.IndividualClient)
class IndividualAdmin(admin.ModelAdmin):
    pass


@admin.register(models.IndividualNationality)
class NationalityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrganisationClient)
class OrganisationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PassportImage)
class PassportImageAdmin(admin.ModelAdmin):
    pass
