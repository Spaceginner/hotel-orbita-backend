from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from hotel.models import Hotel
from hotel_service.models import MealPlan, Service, AdditionalOption


class Building(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='buildings', related_query_name='building', on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    name = models.CharField(max_length=60)
    is_living = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.hotel}, {self.name} ({self.address})"

    def str_short(self) -> str:
        return f"{self.hotel}, {self.name}"


class Floor(models.Model):
    class Meta:
        unique_together = "building", "level"

    building = models.ForeignKey(Building, related_name='floors', related_query_name='floor', on_delete=models.CASCADE)
    level = models.IntegerField()

    def __str__(self) -> str:
        return f"#{self.level} at {self.building.str_short()}"


class RoomCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"«{self.name}»"


class RoomFeature(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Room(models.Model):
    number = models.IntegerField(validators=[MaxValueValidator(99)])
    floor = models.ForeignKey(Floor, related_name='rooms', related_query_name='room', on_delete=models.CASCADE)
    area = models.FloatField(null=True)
    category = models.ForeignKey(RoomCategory, related_name='rooms', related_query_name='room', on_delete=models.SET_NULL, null=True)
    feature = models.ManyToManyField(RoomFeature, related_name='rooms', related_query_name='room')
    beds = models.IntegerField(validators=[MinValueValidator(1)])
    additional_beds = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1000, blank=True)
    notes = models.TextField(max_length=1000, blank=True)

    specific_price = models.DecimalField(max_digits=8, decimal_places=2)

    included_mealplan = models.ForeignKey(MealPlan, related_name='included_in_rooms', related_query_name='included_in_room', on_delete=models.SET_NULL, null=True)
    included_options = models.ManyToManyField(AdditionalOption, related_name='included_in_rooms', related_query_name='included_in_room')

    is_booking = models.BooleanField(default=False)
    available_options = models.ManyToManyField(AdditionalOption, related_name='available_in_rooms', related_query_name='available_in_room')

    def __str__(self) -> str:
        return f"№{self.floor.level}{self.number:0>2} at {self.floor.building.str_short()}"


class RoomUnavailability(models.Model):
    room = models.ForeignKey(Room, related_name='states', related_query_name='state', on_delete=models.CASCADE)

    class Reason(models.TextChoices):
        CLEANING = 'CL', 'Cleaning'
        MAINTENANCE = 'MT', 'Maintenance'

    reason = models.CharField(max_length=2, choices=Reason)

    date_from = models.DateField()
    date_till = models.DateField(null=True)

    @property
    def reason_(self) -> Reason:
        return self.Reason(self.reason)

    def __str__(self) -> str:
        return f"{self.date_from.strftime("%d.%m.%Y")}-{self.date_till.strftime("%d.%m.%Y") if self.date_till is not None else '?'} ({self.reason_})"


class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='images', related_query_name='image', on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    image_description = models.CharField(max_length=150)

    def _get_image_path(self, filename: str) -> str:
        return f"rooms/{self.room.pk}/{self.pk}-{filename}"

    image = models.ImageField(upload_to=_get_image_path)

    def __str__(self) -> str:
        return f"<{self.image.name}> for {self.room}"
