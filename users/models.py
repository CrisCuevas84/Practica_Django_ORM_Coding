from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    edad = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __repr__(self):
        return f"<Usuario object: {self.nombre} {self.apellido}>"
