# Exercício

from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Departamento(Base):
    __tablename__ = "departamentos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    funcionarios = relationship("Funcionario", back_populates="departamento")

    def __init__(self, nome):
        self.nome = nome

    #Função para imprimir
    def __repr__(self):
        return f"Departamento =  id={self.id} - nome={self.nome}"

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cargo = Column(String(100), nullable=False)
    salario = Column(Float, nullable=False)

    departamento_id = Column(Integer, ForeignKey("departamentos.id"))

    #Relacionamento
    departamento = relationship("Departamento", back_populates="funcionarios")

    def __init__(self, nome, cargo, salario, departamento):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.departamento = departamento

    #Função para imprimir
    def __repr__(self):
        return f"Funcionarios =  id={self.id} - nome={self.nome} - cargo={self.cargo}"


engine = create_engine("sqlite:///empresa.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


# with Session() as session:
#     try:
#         #Criando os departamentos
#         ti = Departamento(nome="Tecnicos de T.I")
#         financeiro = Departamento(nome="Financeiro")

#         #Duas formas de associar os funcionários no departamento 
#         # Opção 1
#         # func1 = Funcionario("Pablo", "Dev Front-end", 2.00)
#         # ti.funcionarios.append(func1)

#         # Opção 2
#         func2 = Funcionario("Gustavo", "Dev Back-end", 20.000, departamento=ti)
#         func3 = Funcionario("Ana Luiza", "Dev Full-stack", 31.00, departamento=ti)
#         func4 = Funcionario("Yasmim", "Gerente Financeiro", 12.00, departamento=financeiro)

#         session.add_all([ti, financeiro])
#         session.commit()
#         print(f"Departamentos e funcionários inseridos!")
   
#     except Exception as erro:
#         session.rollback()
#         print(f"Ocorreu um erro {erro}")

# Função para listar os funcionários
# def listar_funcionarios():
#     #Como abrir uma sessão com o banco?
#     with Session() as session:
#         try:
#             #Buscar todos os funcionários dos departamentos.
#             funcionarios = session.query(Funcionario).all() 
#             for funcionario in funcionarios:
#                 print(f"Nome do funcionario: {funcionario.nome} - Departamento: {funcionario.departamento.nome}")
           
#         except Exception as erro:
#             session.rollback()
#             print(f"Ocorreu um erro {erro}")

# listar_funcionarios()

#Criar a função para listar os departamentos e seus funcionários

def listar_departamentos():
    #Como abrir uma sessão com o banco?
    with Session() as session:
        try:
            departamentos = session.query(Departamento).all() 
            for d in departamentos:
                print(f"\n--- Departamento {d.nome} ---")
                for funcionario in d.funcionarios:
                    print(f"Nome: {funcionario.nome} - Cargo {funcionario.cargo} - salario: R$ {funcionario.salario}")
           
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")

listar_departamentos()





    
