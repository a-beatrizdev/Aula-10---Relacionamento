#SQLALCHEMY + ORM
# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# Tabelas do banco
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    def __init__(self, nome):
        self.nome = nome
    
    #Função para imprimir
    def __repr__(self):
        return f"Usuario - id={self.id} - nome={self.nome}"
    
class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(100), nullable=False)

    #Chave estrangeira
    # Onde tem o foreign key, tem o relacionamento muitos para um (muitos pedidos para um usuário
    usuario_id = Column(Integer, ForeignKey())

    def __init__(self, produto):
        self.produto = produto

    def __repr__(self):
        return f"Pedido - id={self.id} - Produto={self.produto}"
    

    
    






