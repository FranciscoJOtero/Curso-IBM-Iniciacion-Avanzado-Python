from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Creamos el correo
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["frankyzarzu@gmail.com"],
                reply_to=[email]
            )

            #Lo enviamos y redireccionamos
            try:
                email.send()
                # Ha ido Bien, redireccionamos a OK
                return redirect(reverse('contact')+"?Ok")
            except:
                #Algo no ha ido Bien, redireccionamos a Fail
                return redirect(reverse('contact')+"?fail")
    
    return render(request, "contact/contact.html", {'form': contact_form})
