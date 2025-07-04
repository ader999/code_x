# Generated by Django 5.2.2 on 2025-06-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smart_exel", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="plantillaexcel",
            name="enlace_descarga",
        ),
        migrations.RemoveField(
            model_name="plantillaexcel",
            name="imagen_url",
        ),
        migrations.AddField(
            model_name="plantillaexcel",
            name="archivo_plantilla",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="plantillas_excel/",
                verbose_name="Archivo de Plantilla",
            ),
        ),
        migrations.AddField(
            model_name="plantillaexcel",
            name="imagen_vista_previa",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="imagenes_plantillas/",
                verbose_name="Imagen de Vista Previa",
            ),
        ),
    ]
