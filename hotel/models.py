from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Hotel(models.Model):
    name = models.CharField(max_length=50)

    def _get_image_path(self, filename: str) -> str:
        return f"hotels/{self.pk}/{filename}"

    image = models.ImageField(upload_to=_get_image_path, null=True)
    address = models.CharField(max_length=300, null=True, blank=False)
    phone_numer = PhoneNumberField(null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    website = models.URLField(null=True, blank=False)

    check_in = models.TimeField(null=False)
    check_out = models.TimeField(null=False)
    check_window = models.FloatField(null=False)

    def __str__(self):
        return f"«{self.name}»"
