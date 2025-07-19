from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.db.models import CheckConstraint, Q
from phonenumber_field.modelfields import PhoneNumberField

from hotel_finances.models import Price


class IndividualNationality(models.Model):
    code = models.CharField(max_length=3, primary_key=True, validators=[MinLengthValidator(3)])

    def __str__(self) -> str:
        return f"{self.code}"


class IndividualClient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, blank=True)

    nationality = models.ForeignKey(IndividualNationality, related_name='clients', related_query_name='client', on_delete=models.SET_NULL, null=True)

    birthday = models.DateField()

    passport_number = models.CharField()
    passport_date = models.DateField()
    passport_issuer = models.CharField()

    def __str__(self) -> str:
        return f"{self.first_name[0]}. {self.patronymic and f"{self.patronymic}."} {self.last_name}"


class PassportImage(models.Model):
    individual = models.ForeignKey(IndividualClient, related_name='passport_images', related_query_name='passport_image', on_delete=models.CASCADE)
    page = models.IntegerField(validators=[MinValueValidator(1)])

    def _get_image_path(self, filename: str) -> str:
        return f"clients/{self.individual.pk}/passports/{self.page}-{filename}"

    image = models.ImageField(upload_to=_get_image_path)

    def __str__(self) -> str:
        return f"{self.individual}'s №{self.page}"


class OrganisationClient(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self) -> str:
        return f"«{self.name}»"


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

    taxpayer_number = models.CharField(max_length=20, unique=True)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(blank=True, unique=True)

    preferences = models.TextField(max_length=3000)

    class Status(models.TextChoices):
        STANDARD = "SD", "Standard"
        VIP = "VP", "VIP"

    status = models.CharField(max_length=2, choices=Status, default=Status.STANDARD)

    discount = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)

    @property
    def status_(self) -> Status:
        return self.Status(self.status)

    def __str__(self) -> str:
        if self.individual is not None:
            specific = self.individual
        else:
            specific = self.organisation

        return f"{specific} ({self.status_})"
