from http.client import HTTPResponse
from django.shortcuts import render
from Libros.models import *
from Libros.forms import FormularioBusqueda, FormularioCargar

# Create your views here.

def inicio(request):
    return render(request,"Libros/base.html")


def mangas(request):

    listado_libros = Manga.objects.all()

    if request.GET.get("titulo"):

        formulario = FormularioBusqueda(request.GET)

        if formulario.is_valid():
           data = formulario.cleaned_data
           listado_libros = Manga.objects.filter(titulo__icontains= data["titulo"])
           
        return render(request,"Libros/index.html", {"libros": listado_libros, "formulario": formulario})

    else: 
        formulario = FormularioBusqueda()
        return render(request,"Libros/index.html", {"libros": listado_libros, "formulario": formulario})



def comics(request):
    listado_libros = Comics.objects.all()

    return render(request,"Libros/comics.html",{"libros": listado_libros})

def novela(request):
    listado_libros = Novela.objects.all()

    return render(request,"Libros/novelas.html",{"libros": listado_libros})


def cargar_manga(request):
    if request.method == "GET":
        return render(request,"Libros/cargar.html")


    else:
        titulo = request.POST["titulo"]
        autor = request.POST["autor"]
        genero = request.POST["genero"]
        precio = request.POST["precio"]
        manga = Manga(titulo=titulo, autor=autor,genero=genero,precio=precio)
        
        manga.save()

        return render(request,"Libros/cargar.html")

    
def cargar_comics(request):
    if request.method == "GET":
        return render(request,"Libros/cargar.html")


    else:
        titulo = request.POST["titulo"]
        autor = request.POST["autor"]
        genero = request.POST["genero"]
        precio = request.POST["precio"]
        manga = Comics(titulo=titulo, autor=autor,genero=genero,precio=precio)
        
        manga.save()

        return render(request,"Libros/cargar.html")

def cargar_novela(request):
    if request.method == "GET":
        return render(request,"Libros/cargar.html")


    else:
        titulo = request.POST["titulo"]
        autor = request.POST["autor"]
        genero = request.POST["genero"]
        precio = request.POST["precio"]
        manga = Novela(titulo=titulo, autor=autor,genero=genero,precio=precio)
        
        manga.save()

        return render(request,"Libros/cargar.html")







