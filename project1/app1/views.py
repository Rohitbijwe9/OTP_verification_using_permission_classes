from django.shortcuts import render
from django.shortcuts import render
from .models import checkOtp,UseLogin
from .serializer import CheckOtpSerializer,UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail



import random
otpn = random.randint(1000, 9999)  # Generate OTP


class UserLogin(APIView):
    def post(self, request):
        try:
            serializer = UserLoginSerializer(data=request.data)
            if serializer.is_valid():
                user_mail = serializer.validated_data.get('email')
                from_email = settings.EMAIL_HOST_USER
                subject = 'OTP Verification'
                message = f'Your OTP is: {otpn}'
                print('otpn', otpn)
                send_mail(subject, message, from_email, [user_mail])
                return Response({'user_mail': user_mail}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        




from rest_framework import permissions



class OTPVerifiedPermission(permissions.BasePermission):
    
    def has_permission(self, request,view):
        check = CheckOtpSerializer(data=request.data)
        if check.is_valid():
            entr_otp = check.validated_data.get('otp')
            return otpn == entr_otp
        return False

class CheckOtpView(APIView):
    permission_classes = [OTPVerifiedPermission]

    def post(self, request):
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
