from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .forms import FormularioForm
from .models import Formulario

def listado(request):
    """
    Esta funcion muestra un listado de todos los formularios creados
    y estos son enviados al template listado.html
    """
    if request.method == 'GET':
        formularios = Formulario.objects.all()
        return render(request,'listado.html',{'formularios':formularios})

def registroFormulario(request):
    if request.method == 'POST':
        """

        Esta es la primera manera en la que podemos registrar datos en un Modelo,
        obtenemos cada uno de los valores enviados en los campos HTML correspondientes

        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        asunto = request.POST.get('asunto')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        Luego llamamos al ORM de Django y utilizamos create para crear un nuevo formulario
        con los datos capturados del HTML
        formulario = Formulario.objects.create(
            nombre = nombre,apellido = apellido,asunto = asunto,email = email,mensaje = mensaje
        )
        """


        #Esta es la segunda forma, en la que se instancia un Form de Django, el cual
        #representa al HTML basado en un modelo, esta clase FormularioForm se puede
        #visualizar en el archivo forms.py
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal:listado')
    else:
        form = FormularioForm()
    return render(request,'index.html',{'form':form})

def editarFormulario(request,id):
    """
    Para la edición, esta función recibe la clavse primaria del formulario
    y se realiza una consulta de busqueda en la base de datos para obtener
    dicho formulario, luego se pregunta si es GET se envia la informacion y
    si es POST significa que se desea guardar la información por lo que 
    se realiza dicha acción
    """
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
    #realizamos una busqueda del formulario y lo eliminamos de la base de datos
    #con el metodo delete()
    formulario = Formulario.objects.get(id = id)
    formulario.delete()
    #redireccionamos a la ruta asociada al nombre listado ubicado dentro del conjunto de rutas
    #llamadas principal, esto lo ubicas en el archivo urls.py principal del proyecto
    return redirect('principal:listado')
