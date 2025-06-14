"""
Modelo para enlaces a redes sociales.
Permite gestionar los enlaces externos a redes sociales de la empresa con validaciones y organización específica.

"""
# Importamos el módulo `models` desde Django.
# Este módulo contiene las clases necesarias para definir modelos de base de datos.
from django.db import models

# Create your models here.
# Definimos el modelo `Link`, que representa un enlace de redes sociales en el sitio web.
class Link(models.Model):

    # - `SlugField` es un campo de texto corto que solo permite caracteres alfanuméricos, guiones y guiones bajos.
    # - `unique=True` asegura que no haya dos enlaces con el mismo nombre clave.
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)

     # Campo para el nombre de la red social.
    # - `CharField` es un campo de texto corto.
    # - `max_length` especifica la longitud máxima del texto.
    name = models.CharField(verbose_name="Red social", max_length=200)

    # Campo para la URL del enlace.
    # - `URLField` es un campo especializado para almacenar direcciones URL.
    # - `null=True` y `blank=True` permiten que este campo sea opcional (puede estar vacío).
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)

     # Campo para la fecha de creación del enlace.
    # - `auto_now_add=True` establece automáticamente la fecha y hora cuando se crea el objeto.
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    # Campo para la fecha de edición del enlace.
    # - `auto_now=True` actualiza automáticamente la fecha y hora cada vez que se guarda el objeto.
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    # Clase interna `Meta` para configurar metadatos del modelo.
    class Meta:

        # Nombre singular legible para el modelo.
        verbose_name = "enlace"

        # Nombre plural legible para el modelo.
        verbose_name_plural = "enlaces"

        # Orden en que se mostrarán los objetos en el panel de administración o consultas.
        # En este caso, se ordenan por el nombre de la red social (`name`) en orden ascendente.
        ordering = ['name']

    # Método `__str__` para definir cómo se representará el objeto como una cadena.
    def __str__(self):

        # En este caso, se muestra el nombre de la red social.
        return self.name
