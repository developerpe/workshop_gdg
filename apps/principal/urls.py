from django.urls import path
from .views import listado,registroFormulario,editarFormulario,eliminarFormulario
from .views_class import *

urlpatterns = [
    path('',RegistrarFormulario.as_view(), name = 'index'),
    path('listado/',ListarFormulario.as_view(), name = 'listado'),
    path('editar_formulario/<int:pk>/',ActualizarFormulario.as_view(), name = 'editar_formulario'),
    path('eliminar_formulario/<int:pk>/',EliminarFormulario.as_view(), name = 'eliminar_formulario'),
]
