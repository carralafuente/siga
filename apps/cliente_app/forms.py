from django import forms
from apps.cliente_app.models import Cliente

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = [
			'codigo_cliente',
			'razonsocial',
			'rfc',
			'correo',
			'fecha_alta', 
			'estado',
			'vendedor',
		]
		labels = {
			'codigo_cliente': 'Código de cliente',
			'razonsocial': 'Razón Social',
			'rfc': 'RFC',
			'correo': 'Email',
			'fecha_alta': 'Fecha de alta',
			'estado': 'Estado',
			'vendedor': 'Vendedor',
		}
		widgets = {
			'codigo_cliente': forms.TextInput(attrs={'class':'form-control'}),
			'razonsocial': forms.TextInput(attrs={'class':'form-control'}),
			'rfc': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_alta': forms.DateInput(attrs={'class':'form-control'}), 
			'estado': forms.TextInput(attrs={'class':'form-control'}),
			'vendedor': forms.Select(attrs={'class':'form-control'}),
		}