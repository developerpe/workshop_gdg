from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .forms import FormularioForm
from .models import Formulario

class RegistrarFormulario(CreateView):
    model = Formulario
    form_class = FormularioForm
    template_name = 'index.html'
    success_url = reverse_lazy('principal:listado')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['algo'] = 'Hola'
        return context
    """
    def post(self,request,*args,**kwargs):
        pass

    def get(self,request,*args,**kwargs):
        pass    
    """
class ListarFormulario(ListView):
    model = Formulario
    template_name = 'listado.html'
    paginate_by = 2

class ActualizarFormulario(UpdateView):
    model = Formulario
    form_class = FormularioForm
    template_name = 'index.html'
    success_url = reverse_lazy('principal:listado')

class EliminarFormulario(DeleteView):
    model = Formulario
    template_name = 'confirmado_eliminar.html'
    success_url = reverse_lazy('principal:listado')
