from .serializers import *
from rest_framework.viewsets import ModelViewSet
from adefemigreat_backend.helper import StandardResultsSetPagination


class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.prefetch_related("gallery_images")
    serializer_class = GallerySerializer
    pagination_class = StandardResultsSetPagination


class GalleryImageViewSet(ModelViewSet):
    queryset = GalleryImage.objects.select_related("gallery")
    serializer_class = GalleryImageSerializer
    pagination_class = StandardResultsSetPagination
