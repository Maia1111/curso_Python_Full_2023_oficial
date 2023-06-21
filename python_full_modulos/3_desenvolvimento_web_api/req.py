
# Desenvolvimento Web Com APi
# Para que serve uma API 
# API é uma interface de programação de aplicações, ou seja, um conjunto de rotinas e padrões estabelecidos por uma aplicação, para que outras aplicações possam utilizar as funcionalidades dessa aplicação.
# Normalmente para se fazer requisições

# O que é uma API Rest
# Rest é um acrônimo para Representational State Transfer, que significa Transferência de Estado Representacional. É um modelo de arquitetura de software que define um conjunto de restrições a serem usadas para a criação de web services (serviços Web).

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    x = 10
    for i in range(10):
        x += i

    return {"mensagem": "Voces esta na pagina home", "valor": x}




@app.get('/cadastro')
def cadastro():
    return {"mensagem": "Olá mundo"}


@app.get('/login')
def login():
    return {'mensagem': 'login'}




usuarios = [(1, 'José', 'senha123'), (2, 'Marcos', 'minhasenha2')]

@app.post('/usuarios/{id:int}')
def get_usuario(id:int):
    lista = [usuario for usuario in usuarios if usuario[1] == id]
    if len(lista)> 0:
        return {'usuarios': lista}
           
    return {'mensagem': 'Usuario não encontrado'}
        
    

@app.post('/usuarios')
def get_usuario(nome):
    lista = [usuario for usuario in usuarios if usuario[1] == nome]
    if len(lista)> 0:
        return {'usuarios': lista}
           
    return {'mensagem': 'Usuario não encontrado'}
    