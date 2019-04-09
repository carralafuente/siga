from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.RegistroUsuario.as_view(), name="usuario_crear"),
]