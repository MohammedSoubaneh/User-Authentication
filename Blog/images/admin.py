from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(Image):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']