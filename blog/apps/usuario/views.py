from django.shortcuts import redirect, render
from .models import Usuario
from django.contrib.auth.forms import UserChangeForm
from django.utils.datastructures import MultiValueDictKeyError

def ver_perfil(request):

	context = {'usuario': request.user}

	return render(request, "usuario/ver_perfil.html", context)

class UserForm(UserChangeForm):

	class Meta:
		model = Usuario
		fields = ['first_name', 'last_name', 'sexo', 'provincia', 'ciudad', 'email', 'descripcion_propia']

	def __init__(self, *args, **kwargs):

		super(self.__class__, self).__init__(*args, **kwargs)
		self.fields['first_name'].required = False
		self.fields['last_name'].required = False
		self.fields['sexo'].required = False
		self.fields['provincia'].required = False
		self.fields['ciudad'].required = False
		self.fields['email'].required = False
		self.fields['descripcion_propia'].required = False


def editar_perfil(request, usuario_id):

	instancia = Usuario.objects.get(id=usuario_id)

	form = UserForm(instance=instancia)

	if request.method == 'POST':
		form = UserForm(request.POST, instance=instancia)

	if form.is_valid():

		instancia = form.save(commit=False)
		instancia.save()

		return redirect('ver_perfil')

	return render(request, "usuario/editar_perfil.html", {'form': form})
# Create your views here.
