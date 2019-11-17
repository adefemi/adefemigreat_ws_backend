from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()
    description = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)


class ProjectImage(models.Model):
    image = models.TextField()
    project = models.ForeignKey(Project, related_name="project_images", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"images {self.project.title}"

    class Meta:
        ordering = ("-created_at",)
