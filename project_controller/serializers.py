from rest_framework.serializers import ModelSerializer
from .models import *


class ProjectImageSerializer(ModelSerializer):

    class Meta:
        model = ProjectImage
        fields = "__all__"


class ProjectSerializer(ModelSerializer):

    project_images = ProjectImageSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = "__all__"
