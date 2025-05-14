#IMPORTACIONES
#Importa varios tipos de campos de formulario:
    #HiddenField: campo oculto (no visible en la interfaz).
    #StringField: campo de texto para cadenas (por ejemplo, nombres, apellidos).
    #SubmitField: botón de envío del formulario.
    #IntegerField: campo numérico (por ejemplo, una membresía representada con un número).
from wtforms import HiddenField, StringField, SubmitField, IntegerField
#Importa el validador DataRequired, que se utiliza para asegurar que el campo no esté vacío al enviar el formulario. 
# Si el usuario deja el campo vacío, se mostrará un mensaje de error y no se enviará el formulario.
from wtforms.validators import DataRequired
#Importa FlaskForm, la clase base que se debe usar en Flask para trabajar con WTForms.
#Esta clase proporciona integración automática con el sistema de sesiones y CSRF de Flask.
from flask_wtf import FlaskForm

#DefinIR la clase ClienteForma, que representa el formulario del cliente en la aplicación. 
#Hereda de FlaskForm, lo cual permite usarlo directamente en las plantillas HTML con Flask y tener validaciones incluidas.
class ClienteForma(FlaskForm):
    #Campo oculto que guarda el id del cliente. Es útil para editar un cliente ya existente sin mostrar el identificador al usuario.
    #Si el valor está vacío, se entiende que es un cliente nuevo. Si tiene un valor, se entiende que se está editando.
    id = HiddenField('id')
    #Campo de texto para introducir el nombre del cliente. El validador DataRequired() obliga a que el campo no pueda quedar vacío.
    nombre = StringField('Nombre', validators=[DataRequired()])
    #Igual que el campo anterior, pero para el apellido del cliente.
    apellido = StringField('Apellido', validators=[DataRequired()])
    #Campo numérico que espera un valor entero, como un código de tipo de membresía o número de cliente. 
    #También incluye la validación para asegurar que no esté vacío.
    membresia = IntegerField('Membresia', validators=[DataRequired()])
    #Botón que aparece en el formulario para enviar los datos. El texto que aparece en el botón será “Guardar”.
    guardar = SubmitField('Guardar')