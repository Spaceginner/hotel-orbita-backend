from rest_framework import serializers

from . import models


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Floor
        fields = 'pk', 'level', 'building_pk'

    pk = serializers.IntegerField(read_only=True)
    building_pk = serializers.IntegerField(write_only=True)


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Building
        fields = 'pk', 'address', 'name', 'is_living', 'floors'

    pk = serializers.IntegerField(read_only=True)
    floors = FloorSerializer(many=True, read_only=True)


class RoomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomCategory
        fields = 'pk', 'name', 'description', 'price'

    pk = serializers.IntegerField(read_only=True)


class RoomFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomFeature
        fields = 'pk', 'name', 'description'

    pk = serializers.IntegerField(read_only=True)
