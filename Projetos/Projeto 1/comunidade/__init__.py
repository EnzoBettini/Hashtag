from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
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

from comunidade import routes
