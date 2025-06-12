"""
Definición del formulario de contacto.

Crea un formulario con validaciones básicas y estilizado para Bootstrap.
Incluye tres campos: nombre, email y contenido del mensaje.
"""

from django import forms

class ContactForm(forms.Form):
    """
    Formulario para que los usuarios envíen mensajes de contacto.
    
    Campos:
        - name: Texto con longitud entre 4-20 caracteres
        - email: Validación automática de formato email
        - content: Texto largo con longitud entre 6-150 caracteres
        
    Todos los campos son obligatorios (required=True) y tienen estilos Bootstrap.
    """

    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Escriba su nombre"}
    ), min_length=4, max_length=20)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder': "Escriba su email"}
    ), min_length=4, max_length=20)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows':3, 'placeholder': "Escriba su mensaje"}
    ),  min_length=6, max_length=150)