"""
    Configuración del panel de administración para la app blog.

    Personaliza cómo se muestran y gestionan los modelos Category y Post en el admin de Django.
"""
from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ''' Personalización del modelo de Category (categorias) en el admin.'''
    readonly_fields = ('created', 'updated') # Campos de solo lectura (creación y última fecha de modificación)

class PostAdmin(admin.ModelAdmin):
    """Personalización avanzada del modelo Post en el admin."""
    readonly_fields = ('created', 'updated') # Campos automáticos no editables

    # Configuración de visualización en lista
    list_display = ('title', 'author', 'published', 'post_categories') # Columnas visibles
    ordering = ('author', 'published') # Orden predeterminado
    search_fields = ('title','content', 'author__username', 'categories__name') # Búsqueda integrada
    date_hierarchy = 'published' # Navegación por fechas
    list_filter = ('author__username','categories__name') # Filtros laterales

    # Método custom para mostrar categorías en list_display
    def post_categories(self, obj):
        """Concatena las categorías del post en un string (para list_display)."""
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    
    post_categories.short_description = "Categorías" # Renombra la columna

# Registro de modelos con sus configuraciones personalizadas
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

'''
Funcionalidades clave:
    Personalización del Admin:
        * readonly_fields: Protege campos automáticos (created/updated) de modificaciones.
        * list_display: Muestra campos adicionales (como el método custom post_categories).

    Optimización de UX:

        * search_fields: Búsqueda en contenido, título y relaciones (autor/categorías).

        * date_hierarchy: Navegación jerárquica por fechas.

        * list_filter: Filtrado lateral por autor y categorías.

    Método Custom:
        * post_categories(): Resuelve la relación many-to-many para mostrar nombres de categorías directamente en la lista de posts.
'''