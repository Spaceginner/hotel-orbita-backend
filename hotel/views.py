from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class HotelViewSet(ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelSerializer

    pagination_class = None
