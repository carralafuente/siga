from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from apps.trabajador_app.forms import TrabajadorForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.trabajador_app.models import Trabajador
# Create your views here.

def index_trabajador(request):
	return render(request, 'trabajador_app/trabajador_app.html')

'''def trabajador_view(request):
	if request.method == 'POST':
		form = TrabajadorForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('trabajador_listar')
	else:
		form = TrabajadorForm()
	return render(request, 'trabajador_app/trabajador_form.html', {'form':form})'''

class TrabajadorList(ListView):
	model = Trabajador
	template_name = 'trabajador_app/trabajador_list.html'	

class TrabajadorCrear(CreateView):
	model = Trabajador
	form_class = TrabajadorForm
	template_name ="trabajador_app/trabajador_form.html"
	success_url = reverse_lazy('trabajador_listar')

class TrabajadorUpdate(UpdateView):
	model = Trabajador
	form_class = TrabajadorForm
	template_name ="trabajador_app/trabajador_form.html"
	success_url = reverse_lazy('trabajador_listar')

class TrabajadorDelete(UpdateView):
	model = Trabajador
	form_class = TrabajadorForm
	template_name ="trabajador_app/trabajador_delete.html"
	success_url = reverse_lazy('trabajador_listar')