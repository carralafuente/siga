from django.db import models
from apps.cliente_app.models import Cliente
# Create your models here.

class Ingreso(models.Model):
	fecha_factura = models.DateField()
	importe = models.CharField(max_length=10)
	factura = models.CharField(max_length=10)
	tipo_producto = models.CharField(max_length=45)
	cliente = models.ForeignKey(Cliente, null = True, blank = True, on_delete=models.CASCADE)
	fecha_proxima = models.DateField()