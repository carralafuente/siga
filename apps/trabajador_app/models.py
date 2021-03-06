from django.db import models

# Create your models here.

class Trabajador(models.Model):
	nombre = models.CharField(max_length=70)
	apellido = models.CharField(max_length=15)
	correo = models.CharField(max_length=70)
	fecha_incorporacion = models.DateField()
	activo = models.BooleanField()
	puesto = models.CharField(max_length=15)

	def __str__(self):
	#Nos permite cambiar los campos de base de datos por sus etiquetas
		return '{} {}'.format(self.nombre, self.apellido)