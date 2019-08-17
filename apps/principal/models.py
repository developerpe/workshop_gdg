from django.db import models

# Create your models here.

class Formulario(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100)
    apellido = models.CharField('Apellido', max_length = 150)
    asunto = models.CharField('Asunto', max_length = 200)
    email = models.EmailField('Email', max_length = 150)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Formulario'
        verbose_name_plural = 'Formularios'

    def _str__(self):
        return self.asunto
