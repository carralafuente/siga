from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.ingreso_app.forms import IngresoForm
# Create your views here.

def index_ingreso(request):
	return render(request, 'ingreso_app/ingreso_app.html')


def ingreso_view(request):
	if request.method == 'POST':
		form = IngresoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index_ingreso')
	else:
		form = IngresoForm()
	return render(request, 'ingreso_app/ingreso_form.html', {'form':form})