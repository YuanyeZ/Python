from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Camera

# Create your views here.
class HomeView(generic.ListView):
    model = Camera
    template_name = 'cam/home.html'

class CameraView(generic.ListView):
    model = Camera
    template_name = 'cam/reviews.html'


