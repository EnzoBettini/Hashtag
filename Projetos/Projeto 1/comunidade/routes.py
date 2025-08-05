from flask import render_template, url_for, request, flash, redirect
from comunidade import app, database, bcrypt
from comunidade.forms import FormCriarConta, FormLogin
from comunidade.models import Usuario
from flask_login import login_user

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
            usuario = Usuario.query.filter_by(email=form_login.email.data).first()
            if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data.encode('utf-8')):
                manter_logado = request.form.get("manter-logado") == "manter-logado"
                login_user(usuario,remember=manter_logado)
                flash(f'Login feito com sucesso no email: {form_login.email.data}', 'alert-success')
                return redirect(url_for('home'))  # ou sua rota principal

            else:
                flash(f'Falha no login, usuario ou senha incorretos', 'alert-danger')

        # Detecta o botão de criar conta
        elif 'botao_submit_criar_conta' in request.form and form_criar.validate():
            usuario = Usuario(username=form_criar.username.data, email=form_criar.email.data, senha=bcrypt.generate_password_hash(form_criar.senha.data).decode('utf-8'))
            database.session.add(usuario)
            database.session.commit()
            flash(f'Conta criada com sucesso no email: {form_criar.email.data}', 'alert-success')
            return redirect(url_for('home'))

    return render_template('login.html', FormCriarConta=form_criar, FormLogin=form_login)
