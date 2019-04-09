from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_cliente, name="index_cliente"),
    path('nuevo/', views.ClienteCrear.as_view(), name="cliente_crear"),
    path('listar/', views.ClienteList.as_view(), name="cliente_listar"),
    path('listar/editar/<int:pk>/', views.ClienteUpdate.as_view(), name="cliente_editar"),
    path('listar/eliminar/<int:pk>/', views.ClienteDelete.as_view(), name="cliente_eliminar"),
]
