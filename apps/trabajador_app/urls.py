from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_trabajador, name='index_trabajador'),
    path('nuevo/', views.trabajador_view, name="trabajador_crear"),
]