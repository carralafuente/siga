from django import forms
from apps.upload_app.models import Upload

class UploadForm(forms.ModelForm):

	class Meta:
		model = Upload

		fields = [
			'fecha',
			'serie',
			'folio',
			'cliente',
			'razonsocial',
			'rfc',
			'estado',
			'neto',
			'descuentos',
			'impuestos',
			'total',
		]
		labels = {
			'fecha':'Fecha',
			'serie':'Serie',
			'folio':'Folio',
			'cliente':'Codigo de cliente',
			'razonsocial':'Razón social',
			'rfc': 'RFC',
			'estado':'Status',
			'neto':'Neto',
			'descuentos':'Descuentos',
			'impuestos':'Impuestos',
			'total':'Total',
		}
