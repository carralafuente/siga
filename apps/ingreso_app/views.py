from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.ingreso_app.forms import IngresoForm
from django.views.generic import ListView
from apps.ingreso_app.models import Ingreso
# Create your views here.

def index_ingreso(request):
	return render(request, 'ingreso_app/ingreso_app.html')


def ingreso_view(request):
	if request.method == 'POST':
		form = IngresoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('ingreso_listar')
	else:
		form = IngresoForm()
	return render(request, 'ingreso_app/ingreso_form.html', {'form':form})

class IngresoList(ListView):
	model = Ingreso
	template_name = 'ingreso_app/ingreso_list.html'	