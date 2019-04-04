from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.cliente_app.forms import ClienteForm

# Create your views here.

def index_cliente(request):
	return render(request, 'cliente_app/cliente_app.html')


def cliente_view(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index_cliente')
	else:
		form = ClienteForm()
	return render(request, 'cliente_app/cliente_form.html', {'form':form})