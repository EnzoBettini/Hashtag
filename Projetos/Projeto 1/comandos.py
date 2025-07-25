from comunidade import app, database
from comunidade.models import Usuario


with app.app_context():
    # database.drop_all()
    # database.create_all()


    # usuario = Usuario(username='Enzo', email='enzoteste@gmail.com', senha='123456')
    # database.session.add(usuario)
    # database.session.commit()
    # meu_post = Post(id_usuario=1, titulo='Meu primeiro post', corpo='caraca mlk postei esse bagui aq')
    # database.session.add(meu_post)
    # database.session.commit()
    usuario_livro = database.session.query(Usuario).filter_by(username='Enzo Teste 2').first()
    # post_visu = database.session.query(Post).filter_by(id_usuario=1).first()
    print(usuario_livro.username)
    print(usuario_livro.email)
    print(usuario_livro.senha)
    # print(usuario_livro.foto_perfil)
    # print(usuario_livro.id)
    # print(usuario_livro.cursos)
    # print(post_visu.autor.email)
