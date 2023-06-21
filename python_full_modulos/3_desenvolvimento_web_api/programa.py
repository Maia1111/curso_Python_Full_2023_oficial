from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, session
from ORM_sqlAlchemy import CONN, Pessoa , Tokens
from secrets import token_hex

app = FastAPI()

def  conectaBanco():
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session




@app.post('/login')
def login(usuario:str, senha:str):
    session = conectaBanco()
    usuarios = session.query(Pessoa).filter_by(usuario=usuario, senha=senha).all()
    if len(usuarios) == 0:
        return 'Usuário não cadastrado!'
    
    
    while True:
        token = token_hex(50)
        tokens = session.query(Tokens).filter_by(token=token).all()
        if len(tokens) == 0:
            
            if len(usuarios) == 0:
                token = Tokens(id_pessoa=usuarios[0].id, token=token)
                session.add(token)
                session.commit() 

            elif len(usuarios) > 0:
                usuarios[0].token = token
                session.add(usuarios[0])
                session.commit()
                        
            

            return {token}   