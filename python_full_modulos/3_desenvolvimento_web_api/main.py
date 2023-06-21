from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Usuario(BaseModel):
    id: int 
    nome: str
    senha: str

lista = [Usuario(id=1, nome='Jose', senha='1234' ),
         Usuario(id=2,nome='Marcos',senha='33333'), 
         Usuario(id=3,nome='Maria',senha='1234')]

@app.get('/usuariosListar')
def main():
    return lista

@app.post('/cadastrar')
def cadastrar(usuario: Usuario):
    lista.append(usuario)
    'Usuário Cadastrado!'
    return usuario