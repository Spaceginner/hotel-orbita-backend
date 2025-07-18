from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from . import models, serializers


class DepartmentViewSet(ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

    def get_serializer_context(self):
        hotel = models.Hotel.objects.get(pk=1)  # fixme

        return super().get_serializer_context() | {
            'hotel': hotel
        }


class DesignationViewSet(ReadOnlyModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer


class StaffViewSet(ModelViewSet):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer
