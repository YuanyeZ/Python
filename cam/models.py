from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Camera(models.Model):

    camera_model = models.CharField(max_length=256, primary_key=True)
    brand = models.CharField(max_length=20)

    camera_picture = models.ImageField()
    stars = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                                       MaxValueValidator(5)])

    #release_date = models.DateField(auto_now=False, auto_now_add=False)
    review = models.TextField(default="no review")


    def __unicode__(self):
        return ': '.join([self.brand, self.camera_model])

# class Lens(models.Model):
#
#     Camera = models.ForeignKey(Camera)
#
#     lens_model = models.CharField(max_length=256)
#     brand = models.CharField(max_length=20)
#
#     lens_picture = models.ImageField(height_field=10, width_field=10)
#     stars = models.IntegerField(default=0,)
#
#     def __unicode__(self):
#         return ': '.join([self.brand, self.lens_model])