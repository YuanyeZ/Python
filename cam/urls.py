'''
URLConf helps to map the view to a URL
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^about/', views.AboutView.as_view(), name='about'),

    url(r'^reviews/', views.CameraView.as_view(), name='reviews'),

    url(r'^brands/', views.CameraList.as_view(), name='brands'),
]