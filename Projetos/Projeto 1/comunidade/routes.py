from flask import render_template, url_for, request, flash, redirect
from comunidade import app, database, bcrypt
from comunidade.forms import FormCriarConta, FormLogin, FormEditarPerfil
from comunidade.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required
from PIL import Image
import secrets
import os

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



@app.route("/login/criarconta")
def criar_conta():
    return redirect(url_for('login'))



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
                    return redirect(url_for('home'))
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



def salvar_imagem(imagem):
    code = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    imagem_final = nome + code + extensao
    path = os.path.join(app.root_path, 'static\profile_pictures', imagem_final)
    size = (200, 200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(size)
    imagem_reduzida.save(path)
    return imagem_final



def atualizar_cursos(form):
    lista_cursos = []
    for campo in form:
        if 'curso_' in campo.name:
            if campo.data:
                lista_cursos.append(campo.label.text)
    return ';'.join(lista_cursos)



@app.route("/perfil/editar", methods=['GET', 'POST'])
@login_required
def editar_perfil():
    FormEditar = FormEditarPerfil()

    # Preenche os campos no GET
    if request.method == 'GET':
        FormEditar.username.data = current_user.username
        FormEditar.email.data = current_user.email

        cursos_salvos = set(campo.strip() for campo in (current_user.cursos or '').split(';') if campo.strip())

        for campo in FormEditar:
            if 'curso_' in campo.name:
                campo.data = campo.label.text in cursos_salvos

    if 'botao_submit_trocar_dados' in request.form and FormEditar.validate():
        # 1) Validar a senha do usuário logado
        if not bcrypt.check_password_hash(current_user.senha, FormEditar.senha.data):
            flash('Falha ao atualizar o usuário ou email, senha incorreta', 'alert-danger')
        else:
            # 2) Verificar se o novo email já existe (e não é o do próprio usuário)
            email_novo = (FormEditar.email.data or '').strip()
            email_atual = (current_user.email or '').strip()

            if email_novo != email_atual:
                outro_usuario = Usuario.query.filter_by(email=email_novo).first()
                if outro_usuario and outro_usuario.id != current_user.id:
                    flash('Este e-mail já está em uso por outra conta.', 'alert-danger')
                    # renderiza a página com os erros mantendo o que o usuário digitou
                    foto_perfil = url_for('static', filename=f'profile_pictures/{current_user.foto_perfil}')
                    return render_template('editarperfil.html', foto_perfil=foto_perfil, FormEditarPerfil=FormEditar)

            # 3) Atualizar apenas o current_user
            current_user.username = FormEditar.username.data
            current_user.email = email_novo

            if FormEditar.foto_perfil.data:
                img = salvar_imagem(FormEditar.foto_perfil.data)
                current_user.foto_perfil = img

            current_user.cursos = atualizar_cursos(FormEditar)

            database.session.commit()
            flash(f'Conta atualizada com sucesso no email: {current_user.email}', 'alert-success')
            return redirect(url_for('perfil'))

    foto_perfil = url_for('static', filename=f'profile_pictures/{current_user.foto_perfil}')
    return render_template('editarperfil.html', foto_perfil=foto_perfil, FormEditarPerfil=FormEditar)


