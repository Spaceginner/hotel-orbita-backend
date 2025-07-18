from django.core.validators import MinValueValidator
from django.db import models

from hotel.models import Hotel
from hotel_service.models import MealPlan, Service, AdditionalOption


class Building(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='buildings', related_query_name='building', on_delete=models.CASCADE, null=False)
    is_living = models.BooleanField(null=False)


class Floor(models.Model):
    building = models.ForeignKey(Building, related_name='floors', related_query_name='floor', on_delete=models.CASCADE, null=False)
    level = models.IntegerField()


class RoomCategory(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)


class RoomFeature(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=300, blank=False, null=True)


class Room(models.Model):
    number = models.IntegerField(null=False)
    floor = models.ForeignKey(Floor, related_name='rooms', related_query_name='room', on_delete=models.CASCADE, null=False)
    area = models.FloatField(null=True)
    category = models.ForeignKey(RoomCategory, related_name='rooms', related_query_name='room', on_delete=models.SET_NULL, null=True)
    feature = models.ManyToManyField(RoomFeature, related_name='rooms', related_query_name='room')
    beds = models.IntegerField(validators=[MinValueValidator(1)])
    additional_beds = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1000, null=True, blank=False)
    notes = models.TextField(max_length=1000, null=False, blank=True)

    specific_price = models.DecimalField(max_digits=8, decimal_places=2)

    included_mealplan = models.ForeignKey(MealPlan, related_name='included_in_rooms', related_query_name='included_in_room', on_delete=models.SET_NULL, null=True)
    included_options = models.ManyToManyField(AdditionalOption, related_name='included_in_rooms', related_query_name='included_in_room')

    available_options = models.ManyToManyField(AdditionalOption, related_name='available_in_rooms', related_query_name='available_in_room')


class RoomUnavailability(models.Model):
    room = models.ForeignKey(Room, related_name='states', related_query_name='state', on_delete=models.CASCADE, null=False)

    class Reason(models.TextChoices):
        BOOKING = 'BK', 'Booking'
        CLEANING = 'CL', 'Cleaning'
        MAINTENANCE = 'MT', 'Maintenance'

    reason = models.CharField(max_length=2, choices=Reason, null=False)

    date_from = models.DateField(null=False)
    date_till = models.DateField(null=True)


class RoomCleaning(models.Model):
    room = models.ForeignKey(Room, related_name='cleanings', related_query_name='cleaning', on_delete=models.CASCADE, null=False)


class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='images', related_query_name='image', on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=400)
    image_description = models.CharField(max_length=150)

    def _get_image_path(self, filename: str) -> str:
        return f"rooms/{self.room.pk}/{self.pk}-{filename}"

    image = models.ImageField()
