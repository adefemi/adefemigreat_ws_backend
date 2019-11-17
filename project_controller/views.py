from .serializers import *
from rest_framework.viewsets import ModelViewSet
from adefemigreat_backend.helper import StandardResultsSetPagination


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.prefetch_related("project_images")
    serializer_class = ProjectSerializer
    pagination_class = StandardResultsSetPagination


class ProjectImageViewSet(ModelViewSet):
    queryset = ProjectImage.objects.select_related("project")
    serializer_class = ProjectImageSerializer
    pagination_class = StandardResultsSetPagination
