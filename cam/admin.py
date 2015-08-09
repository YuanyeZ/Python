from django.contrib import admin

# Register your models here.
from .models import Camera

class CameraAdim(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['brand', 'camera_model']}),
        ('stars', {'fields': ['stars']}),
        ('review', {'fields': ['review'], 'classes': ['collapse']}),

    ]

admin.site.register(Camera, CameraAdim)