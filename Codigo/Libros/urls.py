from django.urls import path
from Libros.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #INICIO Y REGISTROS
    path("",inicio, name="inicio"),
    path("login/",iniciar_sesion, name="iniciar_sesion"),
    path("registrar/",registrar_usuario, name="registrar"),
    path("logout/",LogoutView.as_view(template_name="Libros/Registros/logout.html"), name="logout"),
    path("edit/",editar_usuario, name="editar_usuario"),
    path("usuario_creado/", usuario_creado, name="usuario_creado"),
    
    #MANGAS
    path("cargar_mangas/", cargar_mangas),
    path("mangas/", MangasList.as_view(), name='mangas'),
    path("mangas/editar/<pk>", MangasUpdate.as_view(), name='editar_mangas'),
    path("mangas/borrar/<pk>", MangasDelete.as_view(), name='borrar_mangas'),
    path("mangas/<pk>", MangasDetail.as_view(), name= 'buscar_mangas'),
    path("buscar_manga/", buscar_mangas, name="mangas_buscar"),
    

    #COMICS
    path("cargar_comics/", cargar_comics),
    path("comics/", ComicsList.as_view(), name='comics'),
    path("comics/editar/<pk>", ComicsUpdate.as_view(), name='editar_comics'),
    path("comics/borrar/<pk>", ComicsDelete.as_view(), name='borrar_comics'),
    path("comics/<pk>", ComicsDetail.as_view(), name= 'buscar_comics'),
    path("buscar_comics/",buscar_comics, name="comics_buscar"),
    
    
    #NOVELAS
    path("cargar_novelas/", cargar_novelas),
    path("novelas/", NovelasList.as_view(), name='novelas'),
    path("novelas/editar/<pk>", NovelasUpdate.as_view(), name='editar_novelas'),
    path("novelas/borrar/<pk>", NovelasDelete.as_view(), name='borrar_novelas'),
    path("novelas/<pk>", NovelasDetail.as_view(), name= 'buscar_novelas'),
    path("buscar_novela/", buscar_novela, name="novelas_buscar"),
    

    #ABOUT ME
    path("about_me/", about_me, name="about_me"),

    #Tienda en construccion 
    path("construccion/",enconstruccion,name="construccion")
   
    
]
