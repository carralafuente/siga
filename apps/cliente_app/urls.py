from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index_cliente, name="index_cliente"),
]
