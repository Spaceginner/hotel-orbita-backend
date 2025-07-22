from rest_framework import serializers

from hotel_finances.serializers import PriceSerializer
from hotel_service.serializers import MealPlanSerializer, ServiceSerializer, AdditionalOptionSerializer
from . import models


class ReservationPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReservationPackage
        fields = 'pk', 'day_length', 'discount', 'mealplan', 'included_services', 'included_options'

    pk = serializers.IntegerField(read_only=True)

    discount = PriceSerializer()

    mealplan = MealPlanSerializer(read_only=True)
    mealplan_pk = serializers.IntegerField(write_only=True)
    included_services = ServiceSerializer(many=True, read_only=True)
    included_services_pk = serializers.IntegerField(write_only=True)
    included_options = AdditionalOptionSerializer(many=True, read_only=True)
    included_options_pk = serializers.IntegerField(write_only=True)
