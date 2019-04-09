from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_trabajador, name='index_trabajador'),
    path('nuevo/', views.TrabajadorCrear.as_view(), name="trabajador_crear"),
    path('listar/', views.TrabajadorList.as_view(), name="trabajador_listar"),
    path('listar/editar/<int:pk>/', views.TrabajadorUpdate.as_view(), name="trabajador_editar"),
    path('listar/eliminar/<int:pk>/', views.TrabajadorDelete.as_view(), name="trabajador_eliminar"),
]