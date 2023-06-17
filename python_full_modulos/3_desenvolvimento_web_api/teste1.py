import requests


resultado = requests.post('http://127.0.0.1:8000/usuarios', params={"nome":'Caio'})

print(resultado.json())