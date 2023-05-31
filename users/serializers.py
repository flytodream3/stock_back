from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import StockUser


class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = StockUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_admin')

    def get_is_admin(self, x):
        return x.is_superuser


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = StockUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_admin', 'token')

    def get_token(self, x):
        token = RefreshToken.for_user(x)
        return str(token.access_token)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data
