from django.urls import path
from . import views

app_name = 'djangoRT'

urlpatterns = [
    path('', views.index, name='index'),
]