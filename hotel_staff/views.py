import base64
import io

from django.contrib.auth.models import User
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import UploadedFile
from django.db import transaction
from django.db.models import Func, F, Value
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from . import models, serializers


class DepartmentViewSet(ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

    pagination_class = None


class DesignationViewSet(ReadOnlyModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

    pagination_class = None


class StaffViewSet(ModelViewSet):
    queryset = (
        models.Staff.objects
        .select_related('user')
        .prefetch_related('designation', 'designation__department')
        .annotate(full_name=Func(Value('%s %s'), F('user__first_name'), F('user__last_name'), function='FORMAT'))
        .order_by('pk')
    )
    serializer_class = serializers.StaffSerializer

    filterset_fields = 'designation', 'designation__department'
    search_fields = '=user__username', 'full_name', 'user__email', 'phone_number'

    @transaction.atomic
    def perform_create(self, serializer: serializers.StaffSerializer):
        designation = get_object_or_404(models.Designation, pk=serializer.validated_data['designation_pk'])

        user = User.objects.create(
            username=serializer.validated_data['user']['username'],
            first_name=serializer.validated_data['user']['first_name'],
            last_name=serializer.validated_data['user']['last_name'],
            email=serializer.validated_data['user']['email'],
        )

        user.set_password(serializer.validated_data['password'])

        user.groups.add(designation.group)

        user.save()

        image = ImageFile(
            io.BytesIO(base64.b64decode(serializer.validated_data['image'])),
            name="pfp"
        )

        models.Staff.objects.create(
            user=user,
            hotel=self.request.user.staff.hotel,
            salary_coef=serializer.validated_data['salary_coef'],
            phone_number=serializer.validated_data['phone_number'],
            address=serializer.validated_data['address'],
            designation=designation,
            image=image
        )

    @transaction.atomic
    def perform_update(self, serializer: serializers.StaffSerializer):
        designation = get_object_or_404(models.Designation, pk=serializer.validated_data['designation_pk'])

        staff: models.Staff = serializer.instance

        staff.user.username = serializer.validated_data['user']['username']
        staff.user.first_name = serializer.validated_data['user']['first_name']
        staff.user.last_name = serializer.validated_data['user']['last_name']
        staff.user.email = serializer.validated_data['user']['email']

        if password := serializer.validated_data['password']:
            staff.user.set_password(password)

        staff.user.save()

        staff.salary_coef = serializer.validated_data['salary_coef']
        staff.phone_number = serializer.validated_data['phone_number']
        staff.address = serializer.validated_data['address']
        staff.designation = designation

        try:
            image_enc = serializer.validated_data['image']
        except KeyError:
            pass
        else:
            image = ImageFile(
                io.BytesIO(base64.b64decode(image_enc)),
                name="pfp"
            )

            staff.image = image

        staff.save()
