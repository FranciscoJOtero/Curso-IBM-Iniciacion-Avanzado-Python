"""
URL configuration for webpersonal project.

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
"""

"""
    El archivo urls.py en el directorio principal del proyecto Django (webpersonal/urls.py) es el mapeador de URL principal. 
    Su función es definir cómo las URLs que ingresa un usuario en el navegador se "enrutan" o se dirigen a las funciones 
    o clases de vista apropiadas en nuestro código Django. 
    Esencialmente, es el "centro de control de tráfico" de la aplicación web.

"""

#Importa el módulo admin de Django, que es necesario para incluir las URLs del panel de administración.
from django.contrib import admin
#Importa la función path del módulo django.urls. Esta función es la que se utiliza para definir cada ruta URL individual.
from django.urls import path
#mporta el módulo views de nuestra aplicación core. Se le da el alias core_views para evitar posibles conflictos de nombres 
#si otras aplicaciones también tuvieran un módulo views.
from core import views as core_views
# Similar a la línea anterior, importa el módulo views de nuestra aplicación portfolio y le asigna el alias portfolio_views.
from portfolio import views as portfolio_views
# Importa el objeto settings de Django. Esto permite acceder a las configuraciones definidas 
#en nuestro archivo settings.py (como DEBUG, MEDIA_URL, MEDIA_ROOT).
from django.conf import settings

#Esta es la lista principal de patrones de URL del proyecto. 
#Django recorrerá esta lista en orden, intentando hacer coincidir 
#la URL solicitada con uno de los patrones definidos.
urlpatterns = [
    #Este es el patrón URL. La cadena vacía ('') significa que esta ruta coincidirá con la raíz 
    #del sitio web (por ejemplo, http://127.0.0.1:8000/).
    #Esta es la vista que se ejecutará cuando la URL coincida con el patrón. 
    # En este caso, es la función home dentro del módulo views de la aplicación core.
    #name="home": Asigna un nombre a esta URL. Esto es muy útil porque te permite referenciar la URL 
    #en tus plantillas o en tu código Python usando su nombre (por ejemplo, {% url 'home' %}) 
    #en lugar de codificar la URL directamente. 
    #Si cambias la URL en el futuro, solo necesitas actualizarla aquí, y todas las referencias por nombre seguirán funcionando.
    path('', core_views.home, name="home"),

    #about/: Coincide con la URL http://127.0.0.1:8000/about/.
    #core_views.about: La vista about de la aplicación core.
    #name="about": El nombre de la URL.
    path('about/', core_views.about, name="about"),

    #portfolio/: Coincide con la URL http://127.0.0.1:8000/portfolio/.
    #portfolio_views.portfolio: La vista portfolio de la aplicación portfolio.
    #name="portfolio": El nombre de la URL.
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),

    #contact/: Coincide con la URL http://127.0.0.1:8000/contact/.
    #core_views.contact: La vista contact de la aplicación core.
    #name="contact": El nombre de la URL.
    path('contact/', core_views.contact, name="contact"),

    #admin/: Coincide con la URL http://127.0.0.1:8000/admin/.
    #admin.site.urls: Esto le dice a Django que incluya todas las URLs predefinidas del panel de administración 
    #bajo el prefijo admin/. Es una forma de delegar la gestión de URLs a otro módulo de URLs.
    path('admin/', admin.site.urls),
]

#Este bloque de código solo se ejecuta si la variable DEBUG en el settings.py está configurada como True. 
#Esto es fundamental para el desarrollo.
if settings.DEBUG:
    #Importa la función static del módulo django.conf.urls.static. 
    #Esta función ayuda a servir archivos estáticos y de medios durante el desarrollo.
    from django.conf.urls.static import static

    #Esta línea añade patrones de URL adicionales a urlpatterns para servir 
    # los archivos de medios (imágenes, videos, etc. subidos por los usuarios) 
    #directamente desde el servidor de desarrollo de Django.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #settings.MEDIA_URL: Es la URL base que se ha configurado en settings.py (e.g., /media/).
    #document_root=settings.MEDIA_ROOT: Es la ruta del sistema de archivos donde Django encontrará estos archivos de medios.


"""
    ¡Importante!: Esta forma de servir archivos de medios es SOLO para desarrollo. 
    En un entorno de producción, nunca debemos usar Django para servir archivos estáticos o de medios directamente. 
    En su lugar, se usan servidores web dedicados como Nginx o Apache,
    o servicios de almacenamiento en la nube (como Amazon S3, Google Cloud Storage, etc.).

"""

"""
    urls.py es la hoja de ruta de la aplicación. Define qué URL lleva a qué parte de nuestro código (vista) 
    y cómo se organizan esas rutas. Es crucial para la navegabilidad del sitio y el manejo de solicitudes.

"""
