"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    Configuración principal de URLs para el proyecto webempresa.

Define las rutas (endpoints) de la aplicación y las asocia a sus respectivas vistas.
Organiza las URLs de cada app modularmente usando include().

"""
from django.contrib import admin
from django.urls import include, path
from core import views
from django.conf import settings # Para acceder a configuraciones del proyecto

# Lista principal de patrones de URLs
urlpatterns = [
    #Paths del core
    path('', include('core.urls')), # Incluye todas las URLs de la app core
    #path de services
    path('services/', include('services.urls')), # URLs para la app services

    #path de blog
    path('blog/', include('blog.urls')), #URLs del blog

    #path de pages
    path('page/', include('pages.urls')), # URLs de la app pages (páginas de politica de privacidad, aviso legal y cookies)

    #path de contact
    path('contact/', include('contact.urls')), # URLs de la app contact

    #Paths del admin
    # Panel de administración
    path('admin/', admin.site.urls), # URL para el admin de Django
]

# Configuración adicional para servir archivos multimedia en desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    # Habilita la visualización de archivos subidos (media) durante el desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
    Estructura modular:
        Cada app (core, services, etc.) tiene su propio archivo urls.py que se incluye aquí con include(), manteniendo el proyecto organizado.

        Rutas principales:

            '' → Página principal (manejada por core.urls).
            admin/ → Acceso al panel administrativo de Django.

    Configuración para desarrollo:
        El bloque if settings.DEBUG permite servir archivos multimedia (uploads) directamente desde Django durante el desarrollo, pero esto no debe usarse en producción.

    Jerarquía clara:
        Las URLs siguen una lógica semántica:
            services/ → Toda la lógica de servicios
            blog/ → Entradas del blog
            etc.

'''