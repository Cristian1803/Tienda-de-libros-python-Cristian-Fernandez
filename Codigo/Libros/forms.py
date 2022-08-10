from django.forms import Form, CharField,FloatField

# Formulario de busqueda

class FormularioBusqueda(Form):
    titulo = CharField(max_length=150)

class FormularioCargar(Form):
    titulo = CharField(max_length=150)
    autor = CharField(max_length=150)
    genero =CharField(max_length=150)
    precio =FloatField()