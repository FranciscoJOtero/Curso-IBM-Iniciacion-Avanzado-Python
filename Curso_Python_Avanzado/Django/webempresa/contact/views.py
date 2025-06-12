# Importamos las funciones necesarias desde los módulos de Django.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
# Importamos el formulario personalizado `ContactForm` desde el archivo forms.py de esta aplicación.
from .forms import ContactForm

# Create your views here.
# Definimos la vista `contact`, que maneja las solicitudes HTTP relacionadas con el formulario de contacto.
def contact(request):

    # Creamos una instancia del formulario `ContactForm`.
    # Esto se usará para mostrar el formulario vacío cuando la solicitud no sea POST.
    contact_form = ContactForm()

     # Verificamos si la solicitud es de tipo POST (es decir, si el usuario ha enviado el formulario).
    if request.method == "POST":
        # Si es POST, creamos una nueva instancia del formulario con los datos enviados por el usuario.
        contact_form = ContactForm(data=request.POST)

        # Validamos el formulario. Si es válido, procesamos los datos.
        if contact_form.is_valid():
            # Extraemos los datos del formulario validado.
            # Usamos `request.POST.get()` para obtener los valores de los campos del formulario.
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Creamos un correo electrónico usando la clase `EmailMessage`.
            # - El primer argumento es el asunto del correo.
            # - El segundo argumento es el cuerpo del correo, formateado con los datos del usuario.
            # - El tercer argumento es la dirección de correo electrónico del remitente.
            # - El cuarto argumento es una lista de destinatarios.
            # - El parámetro `reply_to` permite especificar una dirección de respuesta.
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", # Asunto del correo
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content), # Cuerpo del correo
                "no-contestar@inbox.mailtrap.io", # Remitente
                ["frankyzarzu@gmail.com"], # Destinatarios
                reply_to=[email] # Dirección de respuesta
            )

             # Intentamos enviar el correo.
            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Si el correo se envía correctamente, redirigimos al usuario a la página de contacto
                # con un parámetro de éxito en la URL (`?Ok`).
                return redirect(reverse('contact')+"?Ok")
            except:
                 # Si ocurre un error al enviar el correo, redirigimos al usuario a la página de contacto
                # con un parámetro de fallo en la URL (`?fail`).
                return redirect(reverse('contact')+"?fail")
    
    # Si la solicitud no es POST o el formulario no es válido, mostramos el formulario nuevamente.
    # Renderizamos la plantilla `contact/contact.html` y le pasamos el formulario como contexto.
    return render(request, "contact/contact.html", {'form': contact_form})
