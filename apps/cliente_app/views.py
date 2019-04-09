from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from apps.cliente_app.forms import ClienteForm
from django.views.generic import ListView, CreateView, UpdateView ,DeleteView
from apps.cliente_app.models import Cliente
# Create your views here.

def index_cliente(request):
	return render(request, 'cliente_app/cliente_app.html')


'''def cliente_view(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('cliente_listar')
	else:
		form = ClienteForm()
	return render(request, 'cliente_app/cliente_form.html', {'form':form})'''

class ClienteList(ListView):
	model = Cliente
	template_name = 'cliente_app/cliente_list.html'

class ClienteCrear(CreateView):
	model = Cliente
	form_class = ClienteForm
	template_name ="cliente_app/cliente_form.html"
	success_url = reverse_lazy('cliente_listar')

class ClienteUpdate(UpdateView):
	model = Cliente
	form_class = ClienteForm
	template_name ="cliente_app/cliente_form.html"
	success_url = reverse_lazy('cliente_listar')

class ClienteDelete(DeleteView):
	model = Cliente
	form_class = ClienteForm
	template_name ="cliente_app/cliente_delete.html"
	success_url = reverse_lazy('cliente_listar')