'''
URLConf helps to map the view to a URL
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^brands/', views.CameraView.as_view(), name='brands'),
]