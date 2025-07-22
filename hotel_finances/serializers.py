from rest_framework import serializers

from . import models


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price
        fields = 'pk', 'fixed', 'relative'

    pk = serializers.IntegerField(read_only=True)

    def update(self, pr: models.Price, data):
        if (fixed := data.get('fixed')) is not None:
            pr.relative = None
            pr.fixed = fixed
        else:
            pr.fixed = None
            pr.relative = data['relative']

        pr.save()


class SeasonSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SeasonSale
        fields = 'pk', 'discount', 'date_from', 'date_to'

    pk = serializers.IntegerField(read_only=True)
    discount = PriceSerializer()
