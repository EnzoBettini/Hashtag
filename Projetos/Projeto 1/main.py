from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)

lista_usuarios = ['enzo', 'carlos', 'isabela']

app.config['SECRET_KEY'] = 'd61fc15acb695169f7179d578ed67cf7'


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route("/login")
def login():
    form_criar = FormCriarConta()
    form_login = FormLogin()
    return render_template('login.html', FormCriarConta=form_criar, FormLogin=form_login)

if __name__  == '__main__':
    app.run(debug=True)
