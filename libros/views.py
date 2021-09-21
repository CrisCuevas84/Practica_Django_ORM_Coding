from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def index(request):
    context = {"autores": Autor.objects.all()}		# sólo se envía todos los autores
    return render(request, "libros/index.html", context)

