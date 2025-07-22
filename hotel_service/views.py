from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class MealPlanViewSet(ModelViewSet):
    queryset = models.MealPlan.objects.all()
    serializer_class = serializers.MealPlanSerializer

    pagination_class = None


class ServiceViewSet(ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

    pagination_class = None


class AdditionalOptionViewSet(ModelViewSet):
    queryset = models.AdditionalOption.objects.all()
    serializer_class = serializers.AdditionalOptionSerializer

    pagination_class = None
