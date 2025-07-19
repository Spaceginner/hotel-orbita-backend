import functools

from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from . import models


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = 'pk', 'image_url', 'image', 'name', 'username', 'designation', 'mobile', 'email', 'address', 'hod', 'department'

    pk = serializers.IntegerField(read_only=True)
    image_url = serializers.ImageField(source='image', read_only=True)
    image = serializers.ImageField(write_only=True)
    username = serializers.CharField(source='user.username')
    name = serializers.SerializerMethodField()
    designation = serializers.CharField(source='designation.group.name')
    department = serializers.CharField(source='designation.department.name')
    mobile = PhoneNumberField(source='phone_number')
    email = serializers.CharField(source='user.email')
    hod = serializers.SerializerMethodField()

    def get_name(self, s: models.Staff) -> str:
        return s.user.get_full_name() or s.user.username

    def get_hod(self, s: models.Staff) -> bool:
        try:
            _ = s.hod
            return True
        except models.Staff.hod.RelatedObjectDoesNotExist:
            return False


class DepartmentSerializer(serializers.ModelSerializer):
    """requires 'hod' context with a HeadOfDepartment|None and hotel: Hotel object"""

    class Meta:
        model = models.Department
        fields = 'id', 'dName', 'img', 'hod', 'mobile', 'email', 'totalStaff'

    id = serializers.IntegerField(source='pk', read_only=True)
    dName = serializers.CharField(source='name')
    img = serializers.SerializerMethodField()
    hod = serializers.SerializerMethodField()
    mobile = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    totalStaff = serializers.SerializerMethodField()

    def _hod(self, dep: models.Department) -> models.HeadOfDepartment | None:
        try:
            return models.HeadOfDepartment.objects.get(
                department=dep,
                staff__hotel=self.context['hotel'],
            )
        except models.HeadOfDepartment.DoesNotExist:
            return None

    def get_img(self, dep: models.Department) -> str:
        hod = self._hod(dep)
        return hod.staff.image.url if hod is not None else ''

    def get_hod(self, dep: models.Department) -> str:
        hod = self._hod(dep)
        return hod.staff.user.get_full_name() if hod is not None else '<no head>'

    def get_totalStaff(self, dep: models.Department) -> int:
        return dep.get_total_staff(self.context['hotel'])


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = 'name',

    name = serializers.CharField(source='group.name')
