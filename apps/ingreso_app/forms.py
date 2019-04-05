from django import forms
from apps.ingreso_app.models import Ingreso

class IngresoForm(forms.ModelForm):

	class Meta:
		model = Ingreso

		fields = [
			'fecha_factura',
			'importe',
			'factura',
			'tipo_producto',
			'cliente',
			'fecha_proxima',
		]
		labels = {
			'fecha_factura': 'Fecha de factura',
			'importe': 'Importe',
			'factura': 'factura',
			'tipo_producto': 'Tipo de producto',
			'cliente': 'Cliente',
			'fecha_proxima': 'Próximo pago',
		}
		widgets = {
			'fecha_factura': forms.DateInput(attrs={'class':'form-control'}),
			'importe': forms.TextInput(attrs={'class':'form-control'}),
			'factura': forms.TextInput(attrs={'class':'form-control'}),
			'tipo_producto': forms.TextInput(attrs={'class':'form-control'}),
			'cliente': forms.Select(attrs={'class':'form-control'}),
			'fecha_proxima': forms.DateInput(attrs={'class':'form-control'}),
		}