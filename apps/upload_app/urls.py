from django.urls import path, include
from . import views


urlpatterns = [
	path('cargar/', views.UploadFile, name='fichero_cargar'),
	path('crear/', views.UploadCrear, name='registro_crear'),
	path('listar/', views.UploadList, name='fichero_listar'),
	path('editar/<int:id_upload>/', views.UploadEdit, name='registro_editar'),#como esta basado en funciones y no en vistas el atributo que se pasa en la url debe ser el mismo que en la función
	path('eliminar/<int:id_upload>/', views.UploadDelete, name='registro_eliminar'),#como esta basado en funciones y no en vistas el atributo que se pasa en la url debe ser el mismo que en la función
]