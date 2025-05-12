#PROXIMAMENTE SE AÑADIRAN COMENTARIOS EXPLICANDO EL CÓDIGO
from wtforms import HiddenField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class ClienteForma(FlaskForm):
    id = HiddenField('id')
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    membresia = IntegerField('Membresia', validators=[DataRequired()])
    guardar = SubmitField('Guardar')