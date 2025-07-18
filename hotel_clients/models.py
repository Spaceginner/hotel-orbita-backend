from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.db.models import CheckConstraint, Q
from phonenumber_field.modelfields import PhoneNumberField

from hotel_finances.models import Price


class IndividualNationality(models.Model):
    code = models.CharField(max_length=3, blank=False, primary_key=True, validators=[MinLengthValidator(3)])


class IndividualClient(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    patronymic = models.CharField(max_length=50, null=False, blank=True)

    nationality = models.ForeignKey(IndividualNationality, related_name='clients', related_query_name='client', on_delete=models.SET_NULL, null=True)

    birthday = models.DateField(null=False)

    passport_number = models.CharField(null=False)
    passport_date = models.DateField(null=False)
    passport_issuer = models.CharField(null=False)


class PassportImage(models.Model):
    individual = models.ForeignKey(IndividualClient, related_name='passport_images', related_query_name='passport_image', on_delete=models.CASCADE, null=False)
    page = models.IntegerField(validators=[MinValueValidator(1)])

    def _get_image_path(self, filename: str) -> str:
        return f"clients/{self.individual.pk}/passports/{self.page}-{filename}"

    image = models.ImageField(upload_to=_get_image_path)


class OrganisationClient(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)


class ClientStatus(models.Model):
    code = models.CharField(max_length=5, blank=False, primary_key=True)


class Client(models.Model):
    class Meta:
        constraints = [
            CheckConstraint(
                name='individual_or_org',
                check=Q(individual__isnull=False) ^ Q(organisation__isnull=False),
            ),
        ]

        permissions = [
            ('set_discount', 'Allow to edit client\'s discount')
        ]

    individual = models.OneToOneField(IndividualClient, related_name='client', on_delete=models.CASCADE, null=True)
    organisation = models.OneToOneField(OrganisationClient, related_name='client', on_delete=models.CASCADE, null=True)

    taxpayer_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(null=True, blank=False, unique=True)

    preferences = models.TextField(max_length=3000)

    discount = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)
