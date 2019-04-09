from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from apps.ingreso_app.forms import IngresoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.ingreso_app.models import Ingreso
# Create your views here.

def index_ingreso(request):
	return render(request, 'ingreso_app/ingreso_app.html')


'''def ingreso_view(request):
	if request.method == 'POST':
		form = IngresoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('ingreso_listar')
	else:
		form = IngresoForm()
	return render(request, 'ingreso_app/ingreso_form.html', {'form':form})'''

class IngresoList(ListView):
	model = Ingreso
	template_name = 'ingreso_app/ingreso_list.html'	

class IngresoCrear(CreateView):
	model = Ingreso
	form_class = IngresoForm
	template_name ="ingreso_app/ingreso_form.html"
	success_url = reverse_lazy('ingreso_listar')

class IngresoUpdate(UpdateView):
	model = Ingreso
	form_class = IngresoForm
	template_name ="ingreso_app/ingreso_form.html"
	success_url = reverse_lazy('ingreso_listar')

class IngresoDelete(DeleteView):
	model = Ingreso
	form_class = IngresoForm
	template_name ="ingreso_app/ingreso_delete.html"
	success_url = reverse_lazy('ingreso_listar')