from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Camera, Review

# Create handlers.

# Create your views here.
class HomeView(generic.ListView):
    model = Camera
    template_name = 'cam/home.html'

class AboutView(generic.ListView):
    model = Camera
    template_name = 'cam/about.html'

class CameraList(generic.ListView):
    model = Camera
    template_name = 'cam/brands.html'

class CameraView(generic.DetailView):
    CameraModel = Camera
    ReviewModel = Review
    template_name = 'cam/reviews.html'




