from django.contrib.auth.models import User
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from . import models


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = 'pk', 'image_url', 'image', 'name', 'password', 'username', 'designation', 'salary_coef', 'mobile', 'email', 'address', 'hod', 'department', 'first_name', 'last_name', 'designation_pk'

    pk = serializers.IntegerField(read_only=True)
    image_url = serializers.ImageField(source='image', read_only=True)
    image = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    name = serializers.SerializerMethodField()
    designation = serializers.CharField(source='designation.group.name', read_only=True)
    designation_pk = serializers.IntegerField(write_only=True)
    salary_coef = serializers.FloatField(write_only=True)
    department = serializers.CharField(source='designation.department.name', read_only=True)
    mobile = PhoneNumberField(source='phone_number')
    email = serializers.CharField(source='user.email')
    hod = serializers.SerializerMethodField()

    def get_name(self, s: models.Staff) -> str:
        if isinstance(s, dict):
            s = User.objects.get(username=s['user']['username']).staff

        return s.user.get_full_name() or s.user.username

    def get_hod(self, s: models.Staff) -> bool:
        if isinstance(s, dict):
            s = User.objects.get(username=s['user']['username']).staff

        try:
            _ = s.hod
            return True
        except models.Staff.hod.RelatedObjectDoesNotExist:
            return False


class DepartmentSerializer(serializers.ModelSerializer):
    """requires hotel: Hotel object"""

    class Meta:
        model = models.Department
        fields = 'pk', 'name'

    pk = serializers.IntegerField(read_only=True)


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = 'pk', 'name', 'department'

    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(source='group.name')
    department = serializers.CharField(source='department.name', read_only=True)
