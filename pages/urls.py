from django.urls import path, include
from . import views
from django.urls import path
from .views import contact_view

urlpatterns = [
  path('', views.index, name="home"),
  path('about', views.about, name='about'),
  path('contact', views.contact, name='contact'),
  path('example-endpoint', views.example_endpoint, name='example_endpoint'),
  path("contact", contact_view, name="contact"),
]
  
