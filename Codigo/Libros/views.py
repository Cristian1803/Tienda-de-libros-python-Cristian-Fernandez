from django.http import HttpResponse
from django.shortcuts import render , redirect
from Libros.models import *
from Libros.forms import FormularioBusqueda, FormularioCargar
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from Libros.forms import UserCustom, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

def inicio(request):
    
  mangas = Manga.objects.all()
  comics = Comics.objects.all()
  novelas = Novela.objects.all()
  contexto ={
    "mangas": mangas,
    "comics": comics,
    "novelas": novelas
  }

  return render(request,"Libros/base.html",contexto)

    
# SECCION DE COMICS
@login_required
def cargar_comics(request):
    if request.method == "GET":
        formulario = FormularioCargar()
        return render(request,"Libros/cargar.html",{"form":formulario})
    
    else:
         formulario= FormularioCargar(request.POST, request.FILES)
         if formulario.is_valid():
            data = formulario.cleaned_data

            libro = Comics(
                titulo= data.get("titulo"),
                autor= data.get("autor"),
                genero=data.get("genero"),
                precio=data.get("precio"),
                imagen_libro=data.get("imagen_libro"))
            libro.save()
            return redirect("inicio")
         return render(request,"Libros/cargar.html",{"form":formulario, "errors" :"Formulario NO valido"})

       
class ComicsList(ListView ):
    model = Comics
    template_name = "Libros/comics_list.html"

    
class ComicsDetail(DetailView):
    model = Comics
    template_name = "Libros/comics_detail.html"

class ComicsCreate(LoginRequiredMixin, CreateView):
    model = Comics
    success_url = "/comics"
    fields = ["titulo","autor","precio","genero","imagen_libro"]

class ComicsUpdate(LoginRequiredMixin,UpdateView):
    model = Comics
    success_url = "/comics"
    fields = ["titulo","autor","precio","genero","imagen_libro"]

class ComicsDelete(LoginRequiredMixin,DeleteView):
    model = Comics
    success_url = "/comics"

def buscar_comics(request):

    listado_comics = Comics.objects.all()

    if request.GET.get("titulo"):
        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_comics = Comics.objects.filter(titulo__icontains = data["titulo"])

        return render(request,"Libros/comics_buscar.html",{"comics":listado_comics, "formulario":formulario})

    else: 
        formulario = FormularioBusqueda()
        return render(request,"Libros/comics_buscar.html",{"comics":listado_comics, "formulario":formulario})





# SECCION DE REGISTROS
def iniciar_sesion(request):
    if request.method == "GET":
        formulario = AuthenticationForm()
        contexto = {
            "form": formulario
        }
        return render (request, "Libros/Registros/login.html", contexto)

    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data =  formulario.cleaned_data

            usuario = authenticate(username=data.get("username") , password=data.get("password"))
            
            if usuario is not None:
                login(request,usuario)
                return redirect("inicio")

            else:
                contexto = {
                    "error" : "Credenciales no validas",
                    "form" : formulario
                }
                return render (request, "Libros/Registros/login.html", contexto)
        else:
            contexto = {
                    "error" : "Usuario o Contraseña incorrectos",
                    "form" : formulario
                }

            return render (request, "Libros/Registros/login.html", contexto)



def registrar_usuario(request):
    if request.method =="GET":
        formulario = UserCustom()
        return render (request,"Libros/Registros/registro.html",{"form": formulario})
            
    else: 
        formulario = UserCustom(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("usuario_creado")

        else: 
            return render(request,"Libros/Registros/registro.html",{"form": formulario, "error": "formulario NO valido"})


@login_required
def editar_usuario(request):
    if request.method == "GET":
        form = UserEditForm(initial={"username": request.user.username, "email": request.user.email})
        return render(request,"Libros/Registros/editar_usuario.html",{"form": form})

    else: 
        form = UserEditForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data

            usuario = request.user

            usuario.username = data["username"]
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.save()
            return redirect("inicio")

        else:
            return render(request,"Libros/Registros/editar_usuario.html",{"form": form})

def usuario_creado(request):
    return render(request,"Libros/Registros/usuario_creado.html")

#SECCION DE MANGAS 

class MangasList(ListView ):
    model = Manga
    template_name = "Libros/mangas_list.html"

    
class MangasDetail(DetailView):
    model = Manga
    template_name = "Libros/mangas_detail.html"



class MangasUpdate(LoginRequiredMixin,UpdateView):
    model = Manga
    success_url = "/mangas"
    fields = ["titulo","autor","precio","genero","imagen_libro"]

class MangasDelete(LoginRequiredMixin,DeleteView):
    model = Manga
    success_url = "/mangas"

@login_required
def cargar_mangas(request):
    if request.method == "GET":
        formulario = FormularioCargar()
        return render(request,"Libros/cargar.html",{"form":formulario})
    
    else:
         formulario= FormularioCargar(request.POST, request.FILES)
         if formulario.is_valid():
            data = formulario.cleaned_data

            libro = Manga(
                titulo= data.get("titulo"),
                autor= data.get("autor"),
                genero=data.get("genero"),
                precio=data.get("precio"),
                imagen_libro=data.get("imagen_libro"))
            libro.save()
            return redirect("inicio")
         return render(request,"Libros/cargar.html",{"form":formulario, "errors" :"Formulario NO valido"})

def buscar_mangas(request):

    listado_mangas = Manga.objects.all()

    if request.GET.get("titulo"):
        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_mangas = Manga.objects.filter(titulo__icontains = data["titulo"])

        return render(request,"Libros/mangas_buscar.html",{"mangas":listado_mangas, "formulario":formulario})

    else: 
        formulario = FormularioBusqueda()
        return render(request,"Libros/mangas_buscar.html",{"mangas":listado_mangas, "formulario":formulario})




#SECCION DE NOVELAS

class NovelasList(ListView ):
    model = Novela
    template_name = "Libros/novelas_list.html"

    
class NovelasDetail(DetailView):
    model = Novela
    template_name = "Libros/novelas_detail.html"

    
class NovelasUpdate(LoginRequiredMixin,UpdateView):
    model = Novela
    success_url = "/novelas"
    fields = ["titulo","autor","precio","genero","imagen_libro"]

class NovelasDelete(LoginRequiredMixin,DeleteView):
    model = Novela
    success_url = "/novelas"

@login_required
def cargar_novelas(request):
    if request.method == "GET":
        formulario = FormularioCargar()
        return render(request,"Libros/cargar.html",{"form":formulario})
    
    else:
         formulario= FormularioCargar(request.POST, request.FILES)
         if formulario.is_valid():
            data = formulario.cleaned_data

            libro = Novela(
                titulo= data.get("titulo"),
                autor= data.get("autor"),
                genero=data.get("genero"),
                precio=data.get("precio"),
                imagen_libro=data.get("imagen_libro"))
            libro.save()
            return redirect("inicio")
         return render(request,"Libros/cargar.html",{"form":formulario, "errors" :"Formulario NO valido"})


def buscar_novela(request):

    listado_novelas = Novela.objects.all()

    if request.GET.get("titulo"):
        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_novelas = Novela.objects.filter(titulo__icontains = data["titulo"])

        return render(request,"Libros/novelas_buscar.html",{"novelas":listado_novelas, "formulario":formulario})

    else: 
        formulario = FormularioBusqueda()
        return render(request,"Libros/novelas_buscar.html",{"novelas":listado_novelas, "formulario":formulario})




# ABOUT ME
def about_me(request):
    return render(request,"Libros/about_me.html")


# Tienda en construccion
def enconstruccion(request):
    return render(request,"Libros/en_construccion.html")
