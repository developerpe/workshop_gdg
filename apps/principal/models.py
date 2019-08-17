from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 150)
    correo = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre



class Formulario(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100)
    apellido = models.CharField('Apellido', max_length = 150)
    asunto = models.CharField('Asunto', max_length = 200)
    referente = models.ForeignKey(Persona, on_delete = models.CASCADE, null = True, blank = True)
    email = models.EmailField('Email', max_length = 150)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Formulario'
        verbose_name_plural = 'Formularios'

    def __str__(self):
        return self.asunto
