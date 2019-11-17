from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("skill-set", SkillSetView)


urlpatterns = [
    path('', include(router.urls)),
    path('setting', SettingView.as_view()),
    path('login', UserLogin.as_view(), name="User_Login"),
    path('register', Register.as_view(), name="User_Register")
]
