from django.db import models

class PlantillaExcel(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    archivo_plantilla = models.FileField(upload_to='plantillas_excel/', blank=True, null=True, verbose_name="Archivo de Plantilla")
    imagen_vista_previa = models.ImageField(upload_to='imagenes_plantillas/', blank=True, null=True, verbose_name="Imagen de Vista Previa")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Plantilla de Excel"
        verbose_name_plural = "Plantillas de Excel"
