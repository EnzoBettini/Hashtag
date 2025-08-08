from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import Flask
import os

# Carrega variáveis de ambiente
load_dotenv()
POSTGRES_LINK = os.getenv('POSTGRES_RENDER')


app = Flask(__name__)

lista_usuarios = ['enzo', 'carlos', 'isabela']

app.config['SECRET_KEY'] = 'd61fc15acb695169f7179d578ed67cf7'
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_LINK

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'
login_manager.login_message = 'Página inacessivel, por favor faça login para continuar'

from comunidade import routes
