"""
Modelo para páginas dinámicas de la aplicación.

Permite crear y gestionar páginas editables desde el admin
con contenido enriquecido mediante CKEditor.
"""
# Importamos el módulo `models` desde Django.
# Este módulo contiene las clases necesarias para definir modelos de base de datos.
from django.db import models

# Importamos `RichTextField` desde `ckeditor.fields`.
# Este campo permite almacenar contenido enriquecido (HTML) en la base de datos,
# ideal para editores WYSIWYG como CKEditor.
from ckeditor.fields import RichTextField

# Definimos el modelo `Page`, que representa una página en el sitio web.
class Page(models.Model):

    # Campo para el título de la página.
    # - `CharField` es un campo de texto corto.
    # - `verbose_name` define el nombre legible del campo en el panel de administración.
    # - `max_length` especifica la longitud máxima del texto.
    title = models.CharField(verbose_name="Título", max_length=200)

    # Campo para el contenido de la página.
    # - `RichTextField` permite almacenar contenido enriquecido (HTML).
    # - `verbose_name` define el nombre legible del campo en el panel de administración.
    content = RichTextField(verbose_name="Contenido")

    # Campo para el orden de la página.
    # - `SmallIntegerField` es un campo numérico pequeño.
    # - `default=0` establece un valor predeterminado de 0 si no se proporciona un valor.
    order = models.SmallIntegerField(verbose_name="Orden", default=0)

    # Campo para la fecha de creación de la página.
    # - `auto_now_add=True` establece automáticamente la fecha y hora cuando se crea el objeto.
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    # Campo para la fecha de edición de la página.
    # - `auto_now=True` actualiza automáticamente la fecha y hora cada vez que se guarda el objeto.
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    # Clase interna `Meta` para configurar metadatos del modelo.
    class Meta:

        # Nombre singular legible para el modelo.
        verbose_name = "página"

        # Nombre plural legible para el modelo.
        verbose_name_plural = "páginas"

        # Orden en que se mostrarán los objetos en el panel de administración o consultas.
        # Se ordenan primero por `order` y luego por `title`.
        ordering = ['order','title']

    # Método `__str__` para definir cómo se representará el objeto como una cadena.
    # En este caso, se muestra el título de la página.
    def __str__(self):
        return self.title