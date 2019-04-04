from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_ingreso, name='index_ingreso'),
]