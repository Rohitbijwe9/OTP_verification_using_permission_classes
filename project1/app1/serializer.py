from rest_framework import serializers
from .models import UseLogin,checkOtp



class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=UseLogin


class CheckOtpSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=checkOtp






