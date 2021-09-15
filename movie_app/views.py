from django.shortcuts import render, HttpResponse
from .models import Movie

# Create your views here.
def index(request):
    context = {
        'peliculas': Movie.objects.all()
    }
    return render(request, 'movie_app/index.html', context)