# Generated by Django 4.0.6 on 2022-08-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0006_comics_imagen_libro_delete_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='imagen_libro',
            field=models.ImageField(null=True, upload_to='imagenes_libros'),
        ),
    ]
