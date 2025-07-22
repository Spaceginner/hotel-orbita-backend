from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from hotel_finances.models import Price
from hotel_finances.serializers import PriceSerializer
from . import models


class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MealPlan
        fields = 'pk', 'name', 'description', 'price', 'price_pk'

    pk = serializers.IntegerField(read_only=True)
    price = PriceSerializer(read_only=True)
    price_pk = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        price = get_object_or_404(Price, pk=validated_data['price_pk'])
        mealplan = models.MealPlan.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            price=price,
        )

        return mealplan

    def update(self, instance, validated_data):
        price = get_object_or_404(Price, pk=validated_data['price_pk'])

        instance.name = validated_data['name'],
        instance.description = validated_data['description'],
        instance.price = price

        return instance


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = 'pk', 'name', 'description', 'price', 'price_pk'

    pk = serializers.IntegerField(read_only=True)
    price = PriceSerializer(read_only=True)
    price_pk = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        price = get_object_or_404(Price, pk=validated_data['price_pk'])
        mealplan = models.Service.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            price=price,
        )

        return mealplan

    def update(self, instance, validated_data):
        price = get_object_or_404(Price, pk=validated_data['price_pk'])

        instance.name = validated_data['name'],
        instance.description = validated_data['description'],
        instance.price = price

        return instance


class AdditionalOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdditionalOption
        fields = 'pk', 'name', 'description', 'price', 'price_pk'

    pk = serializers.IntegerField(read_only=True)
    price = PriceSerializer(read_only=True)
    price_pk = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        price = get_object_or_404(Price, pk=validated_data['price_pk'])
        mealplan = models.AdditionalOption.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            price=price,
        )

        return mealplan

    def update(self, instance, validated_data):
        price = get_object_or_404(Price, pk=validated_data['price_pk'])

        instance.name = validated_data['name'],
        instance.description = validated_data['description'],
        instance.price = price

        return instance
