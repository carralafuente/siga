from django.db import models

# Create your models here.

class Ingreso(models.Model):
	fecha_factura = models.DateField()
	importe = models.DecimalField(max_digits=2, decimal_places=2)
	factura = models.CharField(max_length=10)
	tipo_producto = models.CharField(max_length=45)
