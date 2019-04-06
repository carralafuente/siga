from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_cliente, name="index_cliente"),
    path('nuevo/', views.cliente_view, name="cliente_crear"),
    path('listar/', views.ClienteList.as_view(), name="cliente_listar"),
]
