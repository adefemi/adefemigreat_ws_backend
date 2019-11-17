from django.urls import path
from .views import *


urlpatterns = [
    path('login', UserLogin.as_view(), name="User_Login"),
    path('register', Register.as_view(), name="User_Register")
]
