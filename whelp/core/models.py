import uuid

from django.db import models


class File(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    file = models.FileField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class PDFContent(models.Model):
    content = models.TextField()
    file = models.ForeignKey('File', on_delete=models.CASCADE)
