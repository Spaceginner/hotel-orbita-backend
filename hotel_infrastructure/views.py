from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class BuildingViewSet(ModelViewSet):
    serializer_class = serializers.BuildingSerializer

    pagination_class = None

    def get_queryset(self):
        return models.Building.objects.filter(hotel=self.request.user.staff.hotel)

    def create(self, request):
        serializer = serializers.BuildingSerializer(data=request.data, write_only=True)
        serializer.is_valid(raise_exception=True)

        building = models.Building.objects.create(
            hotel=self.request.user.staff.hotel,
            name=serializer.validated_data['name'],
            address=serializer.validated_data['address'],
            is_living=serializer.validated_data['is_living'],
        )

        return Response(data=serializers.BuildingSerializer(building, read_only=True).data)


class FloorViewSet(ModelViewSet):
    serializer_class = serializers.FloorSerializer

    pagination_class = None

    def get_queryset(self):
        return models.Floor.objects.filter(building__hotel=self.request.user.staff.hotel)

    def perform_create(self, serializer: serializers.FloorSerializer):
        building = get_object_or_404(models.Building, pk=serializer.validated_data['building_pk'])

        models.Floor.objects.create(
            building=building,
            level=serializer.validated_data['level'],
        )


class RoomCategoryViewSet(ModelViewSet):
    queryset = models.RoomCategory.objects.all()
    serializer_class = serializers.RoomCategorySerializer

    pagination_class = None


class RoomFeatureViewSet(ModelViewSet):
    queryset = models.RoomFeature.objects.all()
    serializer_class = serializers.RoomFeatureSerializer

    pagination_class = None
