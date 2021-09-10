from django.shortcuts import render, HttpResponse

# Create your views here.
def index(Request):
    return HttpResponse("Oi Mundo")


def primer_metodo(request):
    return HttpResponse(" Página de osos")


def segundo_metodo(request, valor):
    return HttpResponse(f"Pagina de osos número: {valor}")


def tercer_metodo(request, nombre):
    return HttpResponse(f"El nombre del oso es: {nombre}")


def cuarto_metodo(request, valor, nombre):
    return HttpResponse(f"El nombre del oso es: {nombre} y su pagina es la numero: {valor}")


