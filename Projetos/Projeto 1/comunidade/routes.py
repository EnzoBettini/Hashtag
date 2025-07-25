from flask import render_template, url_for, request, flash, redirect
from comunidade import app, database, bcrypt
from comunidade.forms import FormCriarConta, FormLogin
from comunidade.models import Usuario

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contato")
def contato():
    return render_template('contato.html')


@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form_criar = FormCriarConta()
    form_login = FormLogin()

    if request.method == 'POST':
        # Detecta o botão de login
        if 'botao_submit_login' in request.form and form_login.validate():
            flash(f'Login feito com sucesso no email: {form_login.email.data}', 'alert-success')
            return redirect(url_for('home'))  # ou sua rota principal

        # Detecta o botão de criar conta
        elif 'botao_submit_criar_conta' in request.form and form_criar.validate():
            usuario = Usuario(username=form_criar.username.data, email=form_criar.email.data, senha=bcrypt.generate_password_hash(form_criar.senha.data))
            database.session.add(usuario)
            database.session.commit()
            flash(f'Conta criada com sucesso no email: {form_criar.email.data}', 'alert-success')
            return redirect(url_for('home'))

    return render_template('login.html', FormCriarConta=form_criar, FormLogin=form_login)
