from django.db import models


class UseLogin(models.Model):
    email=models.EmailField()




class checkOtp(models.Model):
    otp=models.IntegerField()