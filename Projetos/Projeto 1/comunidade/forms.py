from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criar_conta = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
    email = StringField('Nome de Usuário', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    botao_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_trocar_dados = SubmitField('Alterar Dados')
    foto_perfil = FileField('Atualizar Foto de perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    curso_excel = BooleanField('Excel')
    curso_vba = BooleanField('VBA')
    curso_python = BooleanField('Python')
    curso_apresentacao = BooleanField('Apresentação')

class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo do post', validators=[DataRequired(), Length(2, 50)])
    corpo = TextAreaField('Corpo do post', validators=[DataRequired(), Length(1, 800)])
    botao_submit_criar_post = SubmitField('Criar post')
class FormEditarPost(FlaskForm):
    titulo = StringField('Titulo do post', validators=[DataRequired(), Length(2, 50)])
    corpo = TextAreaField('Corpo do post', validators=[DataRequired(), Length(1, 800)])
    botao_submit_criar_post = SubmitField('Criar post')
