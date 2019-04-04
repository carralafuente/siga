from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_ingreso(request):
	return HttpResponse("Página principal de la app ingreso")
