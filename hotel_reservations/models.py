from django.core.validators import MinValueValidator
from django.db import models

from hotel.models import Hotel
from hotel_clients.models import Client
from hotel_finances.models import Price
from hotel_infrastructure.models import Room
from hotel_service.models import MealPlan, Service, AdditionalOption


class ReservationPackage(models.Model):
    day_length = models.IntegerField(null=True)

    discount = models.ForeignKey(Price, on_delete=models.SET_NULL, null=True)

    mealplan = models.ForeignKey(MealPlan, related_name='packages', related_query_name='package', on_delete=models.SET_NULL, null=True)
    included_services = models.ManyToManyField(Service, related_name='packages', related_query_name='package')
    included_options = models.ManyToManyField(AdditionalOption, related_name='packages', related_query_name='package')


# fixme add a shit ton of validators to stay in touch with the package & available options vs included etc
class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='reservations', related_query_name='reservation', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='reservations', related_query_name='reservation', on_delete=models.CASCADE)

    guests_count = models.IntegerField(validators=[MinValueValidator(1)])

    date_in = models.DateField()
    planned_date_out = models.DateField()
    factual_date_out = models.DateField(null=True)

    early_check_in = models.BooleanField(default=False)
    late_check_out = models.BooleanField(default=False)

    package = models.ForeignKey(ReservationPackage, related_name='reservations', related_query_name='reservation', on_delete=models.SET_NULL, null=True)

    mealplan = models.ForeignKey(MealPlan, related_name='reservations', related_query_name='reservation', on_delete=models.SET_NULL, null=True)
    services = models.ManyToManyField(Service, related_name='reservations', related_query_name='reservation')

    class PaymentType(models.TextChoices):
        QR = 'QR', 'QR'
        POS = 'PS', 'POS'
        CASH = 'CS', 'Cash'
        PREPAID = 'PP', 'Pre-Paid'

    payment_type = models.CharField(max_length=2, choices=PaymentType)

    class Status(models.TextChoices):
        RESERVED = 'RR', 'Reserved'
        CANCELLED = 'CC', 'Cancelled'
        NO_SHOW = 'NS', 'No Show'
        PAYED = 'PY', 'Payed'
        CHECKED_IN = 'CI', 'Checked In'
        CHECKED_OUT = 'CO', 'Checked Out'

    status = models.CharField(max_length=2, choices=Status)


class RoomReservation(models.Model):
    reservation = models.ForeignKey(Reservation, related_name='reserved_rooms', related_query_name='reserved_room', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='reservations', related_query_name='reservation', on_delete=models.SET_NULL, null=True)
    guests_count = models.IntegerField(validators=[MinValueValidator(1)])
    additional_options = models.ManyToManyField(AdditionalOption, related_name='reservations', related_query_name='reservation')
