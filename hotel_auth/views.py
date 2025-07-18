from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignInSerializer


class SignInApiView(APIView):
    def post(self, req: Request) -> Response:
        cred_ser = SignInSerializer(data=req)
        cred_ser.is_valid(raise_exception=True)
        credentials = cred_ser.validated_data

        user = authenticate(req, credentials['username'], credentials['password'])

        if user is None:
            return Response(
                status=401,
                data="invalid password or name",
            )
        else:
            token, _ = Token.objects.get_or_create(user=user)

            return Response(status=200, data={'token': token.key})


class SignOutApiView(APIView):
    def post(self, req: Request) -> Response:
        if req.auth is not None:
            req.auth.delete()

        return Response(status=200)
