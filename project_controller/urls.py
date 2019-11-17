from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("list", ProjectViewSet)
router.register("images", ProjectImageViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
