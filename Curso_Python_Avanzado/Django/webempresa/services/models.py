"""
Modelo para servicios de la empresa.

Define la estructura de datos para los servicios ofrecidos,
incluyendo imágenes y fechas automáticas.
"""
# Importamos el módulo `models` desde Django.
# Este módulo contiene las clases necesarias para definir modelos de base de datos.
from django.db import models

# Definimos el modelo `Service`, que representa un servicio en el sitio web.
class Service(models.Model):
    # Campo para el título del servicio.
    # - `CharField` es un campo de texto corto.
    # - `max_length` especifica la longitud máxima del texto.
    # - `verbose_name` define el nombre legible del campo en el panel de administración.
    title = models.CharField(max_length=200, verbose_name="Título")

    # Campo para el subtítulo del servicio.
    # Similar al campo `title`, pero se utiliza para un subtítulo descriptivo.
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")

    # Campo para el contenido del servicio.
    # - `TextField` es un campo de texto largo, ideal para contenido extenso.
    content = models.TextField(verbose_name="Contenido")

    # Campo para la imagen del servicio.
    # - `ImageField` permite almacenar imágenes.
    # - `upload_to="services"` especifica la carpeta donde se guardarán las imágenes en el servidor.
    image = models.ImageField(verbose_name="Imagen", upload_to="services")

    # Campo para la fecha de creación del servicio.
    # - `auto_now_add=True` establece automáticamente la fecha cuando se crea el objeto.
    created = models.DateField(auto_now_add=True, verbose_name="fecha de cración")

    # Campo para la fecha de edición del servicio.
    # - `auto_now=True` actualiza automáticamente la fecha cada vez que se guarda el objeto.
    updated = models.DateField(auto_now=True, verbose_name="fecha de edición")

    # Clase interna `Meta` para configurar metadatos del modelo.
    class Meta:

         # Nombre singular legible para el modelo.
        verbose_name = "servicio"

        # Nombre plural legible para el modelo.
        verbose_name_plural = "servicios"

        # Orden en que se mostrarán los objetos en el panel de administración o consultas.
        # En este caso, se ordenan por fecha de creación (`created`) en orden ascendente.
        ordering = ['created']

    # Método `__str__` para definir cómo se representará el objeto como una cadena.
    def __str__(self):
        
        # En este caso, se muestra el título del servicio.
        return self.title
