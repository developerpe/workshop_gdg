from django import forms
from .models import Formulario,Persona

"""
Un Form representa contenido HTML asociado a un modelo en especifico, asi se ahorra el trabajo de 
escribirlo manualmente y hacer que Django lo genere por nosotros, se le puede añadir clases que
pueden ser de CSS, id,etc

Aqui se definen widgets los cuales representan campos HTML, por ejemplo TextInput representa a input en HTML
ademas podemos modificar las consultas para campos relacionados, es decir con relaciones
"""


class FormularioForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        #aqui se estan definiendo en el constructor, esta es la forma cool por asi decirlo
        super(FormularioForm, self).__init__(*args, **kwargs)
        self.fields['referente'].widget = forms.Select(attrs= {'class':'form-control input100'})
        self.fields['nombre'].widget = forms.TextInput(attrs= {'class':'input100'})  
        self.fields['referente'].queryset = Persona.objects.all()
        

    class Meta:
        model = Formulario
        fields = '__all__'

        """
        La forma comun o mas simple es definir widgets y labels de esta manera:

        Los labels representan los labels de HTML asociados a los campos
        fields = ['nombre','apellido',...]
        labels = {
            'nombre':'Nombre',
            'apellido':'Apellidos',
            ...
        }
        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'id':'nombre',
                    ...
                }
            ),
            ....
        }
        """
