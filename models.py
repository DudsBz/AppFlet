from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

CONN = 'sqlite:///projectCadProduct.db'  
"""Esta é uma String de Conexão para o banco de dados SQLite. 
Ele especifica o caminho do banco de dados. 
Neste caso, o banco de dados é chamado 'projectCadProduct.db' e está localizado no mesmo diretório do script.
O prefixo 'sqlite:///' indica que estamos usando o SQLite como sistema de gerenciamento de banco de dados.
Uma String de Conexão é uma sequência de caracteres que contém informações necessárias para estabelecer uma conexão com um banco de dados.
Ela geralmente inclui o tipo de banco de dados, o nome do banco de dados, o usuário, a senha e o endereço do servidor.

"""
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Produto(Base):
    __tablename__ = "Produto"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50))
    preco = Column(Float())

Base.metadata.create_all(engine)  # Cria as tabelas no banco de dados se não existirem
