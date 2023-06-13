# Serealização em Python
# Sealização para que serve?

""""

Serealização é o processo de transformar um objeto em uma sequência de bytes para que ele

possa ser armazenado em um arquivo, em um buffer de memória ou transmitido através de uma

rede. O processo inverso é chamado de desserialização.

# Qual utilidade 


A serealização é utilizada quando é necessário armazenar objetos em arquivos ou trafegar

objetos em redes.

"""

# OBS: O módulo Pickle do Python implementa protocolos binários para serializar e desserializar

# um objeto Python.

# OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado

# trabalhar com arquivos pickle vindos de outras pessoas que você não conheça ou de fontes

# desconhecidas.

# Exemplo de Serealização

import pickle

x = 1 

# pickle.dumps(x) -> retorna   b'\x80\x03K\x01.' -> string binária do número 1 serealizado

# pickle.loads(b'\x80\x03K\x01.') -> retorna 1 -> número 1 desserealizado

# Serealizando um objeto

# salvar dentro de um arquivo


x = [1, 2, 3, 4 ,5 ]

arquivo = open('lista.pkl', 'wb')

pickle.dump(x, arquivo)

arquivo.close()


# Desserealizando um objeto

# Abrir o arquivo

arquivo = open('lista.pkl', 'rb')

# Printando sem desserealizar -> vai mostrar um objeto serealizado - um endereço de memória
print(arquivo)

# desserealizar o objeto
y = pickle.load(arquivo)

print(y)



arquivo.close()

# OBS: Ao desserealizar um objeto, ele volta a ser um objeto em Python.

# OBS: Para desserealizar um arquivo, é necessário abrir o arquivo em modo de leitura binária.

# OBS: O módulo Pickle do Python implementa protocolos binários para serializar e desserializar


# um objeto Python.

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome} idade: {self.idade}'
    

# Criando uma lista de objetos

p1 = Pessoas('João', 20)

p2 = Pessoas('Maria', 30)


lista = [p1, p2]

# Serealizando a lista de objetos

with open('lista.pkl', 'wb') as arq:
    pickle.dump(lista, arq)


# Desserealizando a lista de objetos

with open('lista.pkl', 'rb') as arq:
    print(arq)
    lista = pickle.load(arq)

    for i in lista:
        print(i)

# OBS: Ao desserealizar um objeto, ele volta a ser um objeto em Python.
        
