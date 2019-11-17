from django.db import models
import uuid


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)


class GalleryImage(models.Model):
    image = models.TextField()
    gallery = models.ForeignKey(Gallery, related_name="gallery_images", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"images {self.gallery.title}"

    class Meta:
        ordering = ("-created_at",)
