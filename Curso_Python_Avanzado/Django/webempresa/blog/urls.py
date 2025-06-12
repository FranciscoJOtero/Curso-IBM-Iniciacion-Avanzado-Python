"""
    URLs específicas de la aplicación blog.

    Define las rutas para:
    - Listado general de entradas del blog
    - Filtrado por categorías
"""

from django.urls import path
from . import views  # Importa las vistas definidas en views.py


urlpatterns = [
    # Página principal del blog (lista todas las entradas)
    path('', views.blog, name="blog"),

    # Filtrado de entradas por categoría (recibe ID de categoría como parámetro)
    path('category/<int:category_id>/', views.category, name="category"),
   
]

'''
************* Explicación detallada: *********************************************************************************************************
            * Estructura básica:
                - Cada path() define una URL y su vista asociada.
                - El parámetro name permite referenciar la URL en templates ({% url 'nombre' %}) y vistas.

            * Rutas definidas:
                '':
                   - URL: /blog/ (se concatena con la URL raíz del proyecto)
                   - Vista: views.blog (mostrará listado completo de posts)
                   - Nombre: 'blog' (para reverse URL lookup)

                category/<int:category_id>/:
                    - URL dinámica que captura un ID de categoría (ej: /blog/category/3/)
                    - <int:category_id> convierte el segmento URL a entero (lo recibe la vista como parámetro)
                    - Vista: views.category (filtrará posts por categoría)
'''