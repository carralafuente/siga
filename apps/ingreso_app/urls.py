from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_ingreso, name='index_ingreso'),
    path('nuevo/', views.ingreso_view, name="ingreso_crear"),
]