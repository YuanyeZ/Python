from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Camera(models.Model):

    camera_model = models.CharField(max_length=255, primary_key=True)
    brand = models.CharField(max_length=20)

    camera_picture = models.ImageField()#upload_to='/camera_model')
    stars = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                                       MaxValueValidator(5)])

    price = models.FloatField(default=0, validators=[MinValueValidator(0)])

    #release_date = models.DateField(auto_now=False, auto_now_add=False)
    comment = models.CharField(max_length=255, default='Nice DLSR Camera')



    def __unicode__(self):
        return ': '.join([self.brand, self.camera_model])


class Review(models.Model):

    camera = models.ForeignKey(Camera)
    review_date = models.DateField(auto_now=True, auto_now_add=False)
    writer = models.CharField(max_length=20, default='Ted')

    review = models.TextField(default="no reviews")

    def __unicode__(self):
        return ': '.join([self.writer, self.review])
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

class User(models.Model):

    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
