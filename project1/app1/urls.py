from django.urls import path
from .views import UserLogin,CheckOtpView

urlpatterns=[
    path('userlog/',UserLogin.as_view()),
    path('checkotp/',CheckOtpView.as_view())
   

]