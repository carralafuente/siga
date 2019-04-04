from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_cliente(request):
	return render(request, 'cliente_app/cliente_app.html')
