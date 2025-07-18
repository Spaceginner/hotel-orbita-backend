import functools

from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models import Sum
from django.db.models.aggregates import Count

from hotel.models import Hotel
from hotel.validators import is_digit, specific_length


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.name}"

    def get_total_staff(self, hotel: Hotel) -> int:
        return (
            self.designations
                .filter(staff__hotel=hotel)
                .annotate(designation_staff=Count('staff'))
                .aggregate(total_staff=Sum('designation_staff'))['total_staff']
        )


class Designation(models.Model):
    group = models.OneToOneField(Group, related_name='designation', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='designations', related_query_name='designation', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.group.name} ({self.department})"


class DesignationSalary(models.Model):
    designation = models.ForeignKey(Designation, related_name='salaries', related_query_name='salary', on_delete=models.CASCADE, null=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=False)
    salary = models.DecimalField(max_digits=8, decimal_places=2)


class Staff(models.Model):
    user = models.OneToOneField(User, related_name='staff', on_delete=models.CASCADE, primary_key=True)
    hotel = models.ForeignKey(Hotel, related_name='staff', on_delete=models.SET_NULL, null=True)
    salary_coef = models.DecimalField(max_digits=6, decimal_places=3)
    phone_number = models.CharField(validators=[
        functools.partial(is_digit, message='В номере телефона допускаются лишь цифры'),
        functools.partial(specific_length, length=10, message='Длина номера телефона должна быть 10 цифр, вышло {got}')
    ])
    address = models.CharField(max_length=300)
    designation = models.ForeignKey(Designation, related_name='staff', on_delete=models.SET_NULL, null=True)

    def _image_path(self, filename: str) -> str:
        return f'staff/{self.user.id}/{filename}'

    image = models.ImageField(upload_to=_image_path, null=True)

    def __str__(self) -> str:
        return f"{self.user.get_full_name() or f"\"{self.user.username}\""} ({self.designation.group.name})"


class HeadOfDepartment(models.Model):
    staff = models.OneToOneField(Staff, related_name='hod', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='heads', related_query_name='head', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.staff} @ {self.department}"
