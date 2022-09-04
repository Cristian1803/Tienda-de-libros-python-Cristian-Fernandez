from django.forms import Form, CharField,FloatField, EmailField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Formulario de busqueda

class FormularioBusqueda(Form):
    titulo = CharField(max_length=150)

class FormularioCargar(Form):
    titulo = CharField(max_length=150)
    autor = CharField(max_length=150)
    precio =FloatField()
    genero =CharField(max_length=150)
    imagen_libro = ImageField()




class UserCustom(UserCreationForm):
    username = CharField(label = "Usuario")
    email = EmailField()
    password1 = CharField(label = "Contraseña", widget= PasswordInput)
    password2 = CharField(label = "Repetir la contraseña", widget= PasswordInput)

    class Meta: 
        model = User
        fields = ["username","email","password1","password2"]
        help_texts = {"username": "","email":"","password1":"","password2": ""}



class UserEditForm(UserCreationForm):
    username = CharField(label = "Usuario")
    email = EmailField()
    password1 = CharField(label = "Contraseña", widget= PasswordInput)
    password2 = CharField(label = "Repetir la contraseña", widget= PasswordInput)

    class Meta: 
        model = User
        fields = ["username","email","password1","password2"]
        help_texts = {"username": "","email":"","password1":"","password2": ""}










