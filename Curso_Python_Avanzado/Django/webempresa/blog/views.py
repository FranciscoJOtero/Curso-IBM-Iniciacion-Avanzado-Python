"""
    Vistas para la aplicación blog.

    Maneja la lógica de presentación para:
        - Listado general de posts
        - Filtrado de posts por categoría
"""

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    """
        Vista principal del blog. Muestra todos los posts publicados.
        
        Args:
            request: Objeto HttpRequest con los datos de la solicitud.
        
        Returns:
            HttpResponse con el template renderizado y contexto:
            - posts: QuerySet con todos los posts (ordenados por Meta.ordering del modelo)
    """

    posts = Post.objects.all() # Obtiene TODOS los posts (podría agregarse .filter(published__lte=timezone.now()))
    return render(request, "blog/blog.html", {'posts': posts})

def category(request, category_id):
    """
        Vista filtrada por categoría. Muestra posts de una categoría específica.
        
        Args:
            request: Objeto HttpRequest.
            category_id (int): ID de la categoría tomado de la URL.
        
        Returns:
            HttpResponse con template y contexto:
            - category: Objeto Category completo
    """

    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category': category})

'''
    Buenas prácticas:
        - Usar get_object_or_404 en lugar de Category.objects.get() para manejo elegante de errores.
        - Los nombres de templates siguen convención app_name/template_name.html.

'''


