from django.db import models

from hotel_infrastructure.models import Building
from hotel_staff.models import Staff, Designation, Department


class Lock(models.Model):
    building = models.ForeignKey(Building, related_name='locks', related_query_name='locks', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lock_id = models.CharField(max_length=100)


class LockGroup(models.Model):
    name = models.CharField(max_length=50)
    building = models.ForeignKey(Building, related_name='lock_groups', related_query_name='lock_group', on_delete=models.CASCADE)
    locks = models.ManyToManyField(Lock, related_name='groups', related_query_name='group')

    permitted_staff = models.ManyToManyField(Staff, related_name='permitted_lock_groups', related_query_name='permitted_lock_group')
    permitted_designations = models.ManyToManyField(Designation, related_name='permitted_lock_groups', related_query_name='permitted_lock_group')
    permitted_departments = models.ManyToManyField(Department, related_name='permitted_lock_groups', related_query_name='permitted_lock_group')
