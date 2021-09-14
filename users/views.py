from django.shortcuts import render, HttpResponse

# Create your views here.
def indice(request):
    return HttpResponse("Hola desde app users")