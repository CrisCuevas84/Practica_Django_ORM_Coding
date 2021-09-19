from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Libro(models.Model):
    titulo = models.CharField(max_length=60)
    autor = models.ForeignKey(Autor, related_name= "libros", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
