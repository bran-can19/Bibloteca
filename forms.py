from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField
from wtforms.validators import DataRequired

class Librosform(FlaskForm):
    titulo = StringField('Titulo',validators=[DataRequired()])
    fk_autor =IntegerField('Autor ID',validators=[DataRequired()])
    fk_editatorial = IntegerField('Editorial ID',validators=[DataRequired()])
    edicion = IntegerField('Edecion',validators=[DataRequired()])
    submit = SubmitField('Agregar Libro')