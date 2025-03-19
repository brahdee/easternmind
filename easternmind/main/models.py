from django.db import models
from django.contrib import admin
from pictures.models import PictureField
import uuid

class Image(models.Model):
    FORMATS = {
        "F": "Film",
        "O": "Other"
    }

    width_field = models.PositiveIntegerField(default=0)
    height_field = models.PositiveIntegerField(default=0)
    image = PictureField(aspect_ratios=[None], height_field="height_field", width_field="width_field")
    format = models.CharField(choices=FORMATS, max_length=10, default=1)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]


admin.site.register(Image, ImageAdmin)