from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class PriceViewSet(ModelViewSet):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSerializer

    pagination_class = None
