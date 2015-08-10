from django.contrib import admin

# Register your models here.
from .models import Camera, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class CameraAdim(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['brand', 'camera_model']}),
        ('stars', {'fields': ['stars']}),
        ('comments', {'fields': ['comment'], 'classes': ['collapse']}),
    ]
    inlines = [ReviewInline]
    list_display = ('brand', 'camera_model', 'comment')
    search_fields = ['camera_model']

admin.site.register(Camera, CameraAdim)