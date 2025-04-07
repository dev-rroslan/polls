from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name='about'),
    path('contact_view', contact_view, name='contact'),  # Use contact_view here
    path('example-endpoint', views.example_endpoint, name='example_endpoint'),
    path('success', views.success_page, name='success_page'),

]
