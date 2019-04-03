from django.db import models

# Create your models here.


class Cliente(models.Model):
	codigo_cliente = models.IntegerField()
	razonsocial = models.CharField(max_length=70)
	rfc = models.CharField(max_length=15)
	correo = models.EmailField()
	fecha_alta = models.DateField()
	estado = models.CharField(max_length=15)

 
 
