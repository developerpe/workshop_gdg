from django.urls import path
from .views import listado,registroFormulario,editarFormulario,eliminarFormulario
from .views_class import *

"""
Aqui se esta utilizando Vistas Basadas en Clases, las cuales simplifican el trabajo de realización
de un CRUD y de la logica en si, y permiten una escalabilidad del proyecto, toda Vista Basada en Clase
tiene funciones definidas que se ejecutan en un determinado orden, estas funciones las podemos editar
para que contengan la logica que se desea.
Cuando utilizamos Vistas Basadas en Clases se utiliza la funcion .as_view() al enlazarla esto para que
sea reconocida como una sola y no como una clase como tal.


name es un nombre opcional que ayuda a llamar a dicha url con solo colocar ese nombre en funciones como
redirect() o reverse_lazy, tal como se visualiza en el archivo views.py y el archivo views_class.py

"""


urlpatterns = [
    path('',RegistrarFormulario.as_view(), name = 'index'),
    path('listado/',ListarFormulario.as_view(), name = 'listado'),
    path('editar_formulario/<int:pk>/',ActualizarFormulario.as_view(), name = 'editar_formulario'),
    path('eliminar_formulario/<int:pk>/',EliminarFormulario.as_view(), name = 'eliminar_formulario'),
]
