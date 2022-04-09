# import django url
from django.urls import path
from . import views

# create the routes
urlpatterns = [
    path('', views.home, name='home'),
]