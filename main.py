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

    #Relacionamento
    pedidos = relationship("Pedido", back_populates="usuario")

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
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    # Relacionamento
    usuario = relationship("Usuario", back_populates="pedidos")


    def __init__(self, produto):
        self.produto = produto

    def __repr__(self):
        return f"Pedido - id={self.id} - Produto={self.produto}"
    
engine = create_engine("sqlite:///loja.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

with Session() as session:
    #Criando um objeto
    usuario1 = Usuario("Gabriel")

    #Criando os pedidos
    pedido1 = Pedido("Mouse")
    pedido2 = Pedido("Notebook")
    pedido3 = Pedido("TV")

    #Associando pedidos aos usuários
    usuario1.pedidos.append(pedido1)
    usuario1.pedidos.append(pedido2)
    usuario1.pedidos.append(pedido3)

    #Salvar no banco
    session.add(usuario1)
    session.commit() 
    
    


    
    






