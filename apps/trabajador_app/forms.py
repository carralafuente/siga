from django import forms
from apps.trabajador_app.models import Trabajador

class TrabajadorForm(forms.ModelForm):

	class Meta:
		model = Trabajador

		fields = [
			'nombre',
			'apellido',
			'correo',
			'fecha_incorporacion', 
			'activo',
			'puesto',
		]
		labels = {
			'nombre': 'Nombre',
			'apellido': 'Apellidos',
			'correo': 'Email',
			'fecha_incorporacion': 'Fecha de alta en la empresa',
			'activo': 'Activo',
			'puesto': 'Tipo de puesto',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_incorporacion': forms.DateInput(attrs={'class':'form-control'}),
			'activo': forms.CheckboxInput(attrs={'class':'form-control'}),
			'puesto': forms.TextInput(attrs={'class':'form-control'}),
		}