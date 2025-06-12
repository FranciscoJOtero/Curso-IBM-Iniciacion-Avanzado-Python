"""
Modelos de la aplicación blog.

Define la estructura de datos para categorías y entradas del blog,
incluyendo relaciones entre ellas y con el usuario.
"""

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User # Modelo de usuario por defecto de Django

# Create your models here.
class Category(models.Model):
    """
    Modelo para categorizar entradas del blog.
    
    Campos:
        name: Nombre de la categoría (único por defecto).
        created: Fecha automática de creación (no editable).
        updated: Fecha automática de última modificación.
    """

    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría" # Nombre singular en admin
        verbose_name_plural = "categorías" # Nombre plural en admin
        ordering = ['-created'] # Orden descendente por fecha de creación

    def __str__(self):
        """Representación legible del modelo (para admin/consolas)."""
        return self.name
    
class Post(models.Model):
    """
    Modelo para entradas del blog con relaciones a categorías y usuario.
    
    Campos:
        title: Título de la entrada.
        content: Contenido en formato texto largo.
        published: Fecha de publicación (configurable, now() por defecto).
        image: Imagen opcional (guardada en /media/blog/).
        author: Relación ForeignKey con el usuario que crea el post.
        categories: Relación ManyToMany con categorías.
    """

    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created'] # Ordena por creación descendente

    def __str__(self):
        """Representación legible del modelo."""
        return self.title
    

'''
    Puntos destacables:
        * Relaciones clave:
            - ForeignKey(User): Cada post pertenece a un usuario (borrado en cascada).
            - ManyToManyField(Category): Un post puede tener múltiples categorías y viceversa.

        * Campos automáticos:
            - auto_now_add=True: Fija fecha solo al crear.
            - auto_now=True: Actualiza fecha al modificar.

        * Configuración de media:
            - upload_to="blog": Las imágenes se guardan en MEDIA_ROOT/blog/.

        * Buenas prácticas:
            - verbose_name: Nombres legibles para el admin.
            - related_name: Acceso inverso claro (category.get_posts.all()).
'''

