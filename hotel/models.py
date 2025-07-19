from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Hotel(models.Model):
    name = models.CharField(max_length=50)

    def _get_image_path(self, filename: str) -> str:
        return f"hotels/{self.pk}/{filename}"

    image = models.ImageField(upload_to=_get_image_path, null=True)
    address = models.CharField(max_length=300, blank=True)
    phone_numer = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    check_in = models.TimeField()
    check_out = models.TimeField()
    check_window = models.FloatField()

    def __str__(self):
        return f"«{self.name}»"
