from rest_framework import serializers

from hotel_finances.serializers import SeasonSaleSerializer
from . import models


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hotel
        fields = 'name', 'image', 'image_enc', 'address', 'phone_number', 'email', 'website', 'check_in', 'check_out', 'check_window', 'season_sales', 'season_sales_pks'

    image = serializers.ImageField(read_only=True)
    image_enc = serializers.CharField(write_only=True, allow_blank=True, required=False)
    season_sales = SeasonSaleSerializer(many=True, read_only=True)
    season_sales_pks = serializers.ListSerializer(child=serializers.IntegerField(), write_only=True)
