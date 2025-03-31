from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name="home"),
  path('example-endpoint', views.example_endpoint, name='example_endpoint'),
  
]