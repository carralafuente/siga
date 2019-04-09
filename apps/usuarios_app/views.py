from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuarios_app.forms import RegistroForm
# Create your views here.

class RegistroUsuario(CreateView):
	model = User
	template_name = 'usuarios_app/usuarios_registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('cliente_listar')
