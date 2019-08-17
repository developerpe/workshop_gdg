from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .forms import FormularioForm
from .models import Formulario

def listado(request):
    if request.method == 'GET':
        formularios = Formulario.objects.all()
        return render(request,'listado.html',{'formularios':formularios})

def registroFormulario(request):
    if request.method == 'POST':
        """
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        asunto = request.POST.get('asunto')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        formulario = Formulario.objects.create(
            nombre = nombre,apellido = apellido,asunto = asunto,email = email,mensaje = mensaje
        )
        """
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal:listado')
    else:
        form = FormularioForm()
    return render(request,'index.html',{'form':form})

def editarFormulario(request,id):
    formulario = Formulario.objects.get(id = id)
    if request.method == 'GET':
        form = FormularioForm(instance = formulario)
    else:
        form = FormularioForm(request.POST, instance = formulario)
        if form.is_valid():
            form.save()
            return redirect('principal:listado')
    return render(request,'index.html',{'form':form})

def eliminarFormulario(request,id):
    formulario = Formulario.objects.get(id = id)
    formulario.delete()
    return redirect('principal:listado')
