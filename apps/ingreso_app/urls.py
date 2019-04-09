from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_ingreso, name='index_ingreso'),
    path('nuevo/', views.IngresoCrear.as_view(), name="ingreso_crear"),
    path('listar/', views.IngresoList.as_view(), name="ingreso_listar"),
    path('listar/editar/<int:pk>/', views.IngresoUpdate.as_view(), name="ingreso_editar"),
    path('listar/eliminar/<int:pk>/', views.IngresoDelete.as_view(), name="ingreso_eliminar"),
]