import datetime

from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignInSerializer, TokenSerializer


class SignInApiView(APIView):
    permission_classes = []

    @extend_schema(
        request=SignInSerializer,
        responses=TokenSerializer,
    )
    def post(self, req: Request) -> Response:
        cred_ser = SignInSerializer(data=req.data)
        cred_ser.is_valid(raise_exception=True)
        credentials = cred_ser.validated_data
        user = authenticate(req, username=credentials['username'], password=credentials['password'])

        if user is None or datetime.datetime.now(tz=datetime.UTC) < user.date_joined:
            return Response(
                status=401,
                data="invalid password or name, or no access yet",
            )
        else:
            token, _ = Token.objects.get_or_create(user=user)

            return Response(status=200, data={'token': token.key})


class SignOutApiView(APIView):
    def post(self, req: Request) -> Response:
        if req.auth is not None:
            req.auth.delete()

        return Response(status=200)
