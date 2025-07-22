from rest_framework import serializers

from hotel_finances.serializers import SeasonSaleSerializer
from . import models


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hotel
        fields = 'image', 'address', 'phone_number', 'email', 'website', 'check_in', 'check_out', 'season_sales'

    pk = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(read_only=True)
    image_enc = serializers.CharField(write_only=True, allow_blank=True, required=False)
    season_sales = SeasonSaleSerializer(many=True, read_only=True)
    season_sales_pks = serializers.IntegerField(many=True)
