from django.contrib import admin

from . import models


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Designation)
class DesignationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DesignationSalary)
class DesignationSalaryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HeadOfDepartment)
class HodAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    pass
