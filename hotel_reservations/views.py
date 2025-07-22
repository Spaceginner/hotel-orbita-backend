from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class ReservationPackageViewSet(ModelViewSet):
    queryset = models.ReservationPackage.objects.all()
    serializer_class = serializers.ReservationPackageSerializer

    pagination_class = None
