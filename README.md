# Entrega del proyecto final - Python. Fernandez Blejman Cristian

## instrucciones
Biendenidxs!

Primero es necesario instalar Django utilizando el comando pip desde la terminal
```
> pip install django
```

Para correr el proyecto, es necesario utilizar el comando cd hasta estar en el mismo directorio del archivo manage.py (en este caso se encuentra dentro de la carpeta "Codigo")

Primero hay que hacer las migraciones para crear la base de datos.
```
> python manage.py makemigrations
> python manage.py migrate
```
Una vez hecho esto, ya esta listo para correrse. ejecutamos:
```
> python manage.py runserver
```
El inicio de la pagina se mostrara vacio, pero una vez cargados los elementos en nuestra base de datos van a poder verse en nuestra pagina.

## Como agrego elemento a la base de datos?
pueden crear un superusuario e iniciar sesión en la pagina para agregar nuevos libros. 
para eso hay que usar el comando:
```
> python manage.py createsuperuser
```

una vez hecho eso ya pueden iniciar sesión en la pagina y empezar a cargar nuevos libros.


##Adjunto un video mostrando como funciona la pagina:
https://youtu.be/YNEONoW2kA8