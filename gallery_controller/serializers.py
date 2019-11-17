from rest_framework.serializers import ModelSerializer
from .models import *


class GalleryImageSerializer(ModelSerializer):

    class Meta:
        model = GalleryImage
        fields = "__all__"


class GallerySerializer(ModelSerializer):
    gallery_images = GalleryImageSerializer(read_only=True, many=True)

    class Meta:
        model = Gallery
        fields = "__all__"

