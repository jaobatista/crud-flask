from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional

class UserForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    # Senha opcional para permitir edição sem alterar senha
    password = PasswordField('Senha', validators=[Optional(), Length(min=6)])
    submit = SubmitField('Salvar')
