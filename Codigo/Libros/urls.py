from django.urls import path
from Libros.views import *

urlpatterns = [
    path("",inicio),
    path("mangas/", mangas),
    path("comics/", comics),
    path("novelas/", novela),
    path("cargar_mangas/", cargar_manga),
    path("cargar_comics/", cargar_comics),
    path("cargar_novelas/", cargar_novela)
]
