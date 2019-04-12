from django.db import models

# Create your models here.

class Upload(models.Model):
	fecha = models.CharField(max_length=15)
	serie = models.CharField(max_length=1)
	folio = models.CharField(max_length=15)
	cliente = models.CharField(max_length=15)
	razonsocial = models.CharField(max_length=75)
	rfc = models.CharField(max_length=15)
	estado = models.CharField(max_length=15)
	neto = models.CharField(max_length=15)
	descuentos = models.CharField(max_length=15)
	impuestos = models.CharField(max_length=15)
	total = models.CharField(max_length=15)


	def __str__(self):
	#Nos permite cambiar los campos de base de datos por sus etiquetas
		return '{} {} {} {}'.format(self.fecha, self.folio, self.razonsocial, self.total)