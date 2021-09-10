from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.index),
    path('osos', views.primer_metodo),
    path('osos/<int:valor>', views.segundo_metodo),
    path('osos/<str:nombre>/oso', views.tercer_metodo),
    path('<int:valor>/<str:nombre>', views.cuarto_metodo),
]