from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_ingreso(request):
	return render(request, 'ingreso_app/ingreso_app.html')
