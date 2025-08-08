from flask import render_template, url_for, request, flash, redirect
from comunidade import app, database, bcrypt
from comunidade.forms import FormCriarConta, FormLogin, FormEditarPerfil
from comunidade.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contato")
def contato():
    return render_template('contato.html')


@app.route("/usuarios")
@login_required
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
                next_param = request.args.get('next')
                if next_param:
                    return redirect(next_param)
                else:
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

@app.route("/logout")
@login_required
def sair():
    logout_user()
    flash('Logout feito com sucesso!', 'alert-success')
    return redirect(url_for('home'))

@app.route("/perfil")
@login_required
def perfil():
    foto_perfil = url_for('static', filename='profile_pictures/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)

@app.route("/post/criar")
@login_required
def criar_post():
    return render_template('criarpost.html')

@app.route("/perfil/editar", methods=['GET', 'POST'])
@login_required
def editar_perfil():
    FormEditar = FormEditarPerfil()

    # Preenche os campos no GET
    if request.method == 'GET':
        FormEditar.username.data = current_user.username
        FormEditar.email.data = current_user.email

    usuario_verificar = Usuario.query.filter_by(email=FormEditar.email.data).first() if FormEditar.email.data else current_user

    if 'botao_submit_trocar_dados' in request.form and FormEditar.validate():
        if usuario_verificar and bcrypt.check_password_hash(usuario_verificar.senha, FormEditar.senha.data.encode('utf-8')):
            usuario_verificar.username = FormEditar.username.data
            usuario_verificar.email = FormEditar.email.data
            database.session.commit()
            flash(f'Conta atualizada com sucesso no email: {FormEditar.email.data}', 'alert-success')
            return redirect(url_for('perfil'))
        else:
            flash(f'Falha ao atualizar o usuario ou email, senha incorreta', 'alert-danger')

    foto_perfil = url_for('static', filename='profile_pictures/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, FormEditarPerfil=FormEditar)

