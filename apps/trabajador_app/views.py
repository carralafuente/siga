from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.trabajador_app.forms import TrabajadorForm
from django.views.generic import ListView
from apps.trabajador_app.models import Trabajador
# Create your views here.

def index_trabajador(request):
	return render(request, 'trabajador_app/trabajador_app.html')

def trabajador_view(request):
	if request.method == 'POST':
		form = TrabajadorForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('trabajador_listar')
	else:
		form = TrabajadorForm()
	return render(request, 'trabajador_app/trabajador_form.html', {'form':form})

class TrabajadorList(ListView):
	model = Trabajador
	template_name = 'trabajador_app/trabajador_list.html'	