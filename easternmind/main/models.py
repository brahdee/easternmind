from django.db import models
from django.contrib import admin
from pictures.models import PictureField
import uuid


class Image(models.Model):
    width_field = models.PositiveIntegerField(default=0)
    height_field = models.PositiveIntegerField(default=0)
    image = PictureField(
        aspect_ratios=[None], height_field="height_field", width_field="width_field"
    )
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )


class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]


admin.site.register(Image, ImageAdmin)
