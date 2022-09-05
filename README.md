# Entrega del proyecto final - Python. Fernandez Blejman Cristian

## Instrucciones

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
Una vez hecho esto, ya está listo para correrse. Ejecutamos:
```
> python manage.py runserver
```
El inicio de la página se mostrara vacío, pero una vez cargados los elementos en nuestra base de datos van a poder verse en nuestra página.

## ¿Cómo agrego elementos a la base de datos?
Crear un superusuario e iniciar sesión en la página para agregar nuevos libros. 
Para eso hay que usar el comando:
```
> python manage.py createsuperuser
```

Una vez hecho eso ya pueden iniciar sesión en la página y empezar a cargar nuevos libros.


## Adjunto un video mostrando como funciona la página:
https://youtu.be/YNEONoW2kA8