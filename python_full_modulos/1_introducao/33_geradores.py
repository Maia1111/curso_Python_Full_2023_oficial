from  pympler.asizeof import asizeof



# Oque é um gerador em python 
"""
Geradores são funções que retornam um iterador que pode ser iterado apenas uma vez.

O gerador é uma função que retorna um objeto (iterador) que podemos iterar sobre ele (um valor por vez).

"""

print(asizeof([1, 2, 3, 4]))


def dobro(lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i * 2)
    return lista_dobro


x = range(0, 100)
dobro(x)
print(asizeof(dobro(x)))


def dobro():
    i = 0
    while True:
        i += 1
        yield i


x = dobro()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
