from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
import datetime 

USUARIO =  'root'
SENHA = '1234'
HOST = 'localhost'
BANCO = 'aula_FastAPI'
PORT = '3306'

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

# Criando o banco de dados
engine = create_engine(CONN, echo=True)

# Criando uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criando uma classe base
Base = declarative_base()

# Criando a tabela Pessoa
class Pessoa(Base):
    __tablename__ = 'Pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    usuario = Column(String(20))
    senha = Column(String(20))

# Criando a tabela Tokens
class Tokens(Base):
    __tablename__ = 'Tokens'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('Pessoa.id'))
    token = Column(String(100))
    data = Column(DateTime, default=datetime.datetime.utcnow())

# Criando todas as tabelas
Base.metadata.create_all(engine)
