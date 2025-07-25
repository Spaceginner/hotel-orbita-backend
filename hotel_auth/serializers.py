from rest_framework import serializers


class SignInSerializer(serializers.Serializer):
    class Meta:
        fields = 'username', 'password'

    username = serializers.CharField()
    password = serializers.CharField()


class TokenSerializer(serializers.Serializer):
    class Meta:
        fields = 'token'

    token = serializers.CharField()
