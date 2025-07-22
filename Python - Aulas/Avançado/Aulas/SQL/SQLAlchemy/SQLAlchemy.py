from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()
POSTGRES_LINK = os.getenv('POSTGRES_RENDER')

# Conexão e sessão
db = create_engine(POSTGRES_LINK)
Session = sessionmaker(bind=db)
session = Session()

# Base ORM
Base = declarative_base()

# Modelo Usuario
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__ (self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo

# Modelo Livro
class Livro(Base):
    __tablename__ = "livros"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__ (self, titulo, qtde_paginas, dono):
        self.dono = dono
        self.qtde_paginas = qtde_paginas
        self.titulo = titulo

# Criação das tabelas no banco
Base.metadata.create_all(bind=db)


# usuario = Usuario(nome='burgas', email='aaaaaa@aaaa.com.br', senha='123123')
# session.add(usuario)
# session.commit()

# lista_usuarios = session.query(Usuario).all()
usuario_livro = session.query(Usuario).filter_by(nome='burgas').first()
print(usuario_livro.nome)
print(usuario_livro.email)
print(usuario_livro.senha)
print(usuario_livro.ativo)
print(usuario_livro.id)


livro = Livro(titulo='Turma da Mônica', qtde_paginas='50', dono=usuario_livro.id)
session.add(livro)
session.commit()


session.delete(usuario_livro)
session.commit()
