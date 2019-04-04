from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_trabajador(request):
	return render(request, 'trabajador_app/trabajador_app.html')
