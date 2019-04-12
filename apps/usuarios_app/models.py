from django.db import models

# Create your models here.

class RegistroUsuario(models.Model):

	username = models.CharField(max_length=15)
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	email = models.EmailField()
	

	def __str__(self):
	#Nos permite cambiar los campos de base de datos por sus etiquetas
		return '{} {}'.format(self.nombre, self.apellido)