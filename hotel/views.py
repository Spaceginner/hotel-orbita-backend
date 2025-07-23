import base64
import io

from django.core.files.images import ImageFile
from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from . import models, serializers


class HotelViewSet(GenericViewSet):
    queryset = models.Hotel.objects.none()

    def check_permissions(self, request: Request) -> None:
        if request._request.method not in ['GET', 'OPTIONS']:
            super().check_permissions(request)

    @extend_schema(
        request=None,
        responses=serializers.HotelSerializer
    )
    def retrieve(self, req: Request):
        hotel = req.user.staff.hotel

        return Response(serializers.HotelSerializer(hotel).data)

    @extend_schema(
        request=serializers.HotelSerializer,
        responses=None
    )
    def update(self, req: Request, partial: bool = False) -> Response:
        ser = serializers.HotelSerializer(data=req.data, write_only=True)
        ser.is_valid(raise_exception=True)
        data = ser.validated_data

        hotel = req.user.staff.hotel

        hotel.name = data['name']
        hotel.address = data['address']
        hotel.phone_number = data['phone_number']
        hotel.email = data['email']
        hotel.website = data['website']
        hotel.check_in = data['check_in']
        hotel.check_out = data['check_out']
        hotel.check_window = data['check_window']

        if (image_enc := ser.validated_data.get('image_enc')) is not None:
            image = ImageFile(
                io.BytesIO(base64.b64decode(image_enc)),
                name="image"
            )

            hotel.image = image

        hotel.save()

        return Response()

