from django.urls import path

from . import views

urlpatterns = [
    path('', views.djmodels, name= "djmodels"),
]