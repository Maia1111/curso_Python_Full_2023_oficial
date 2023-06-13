# Uma lista é uma estrutura que pode armazenar vários dados um uma unica variável

# Criando uma lista vazia
lista = []

nomes = ['Caio', 'Marcos', 'João', 'Pedro']
print(type(nomes))
print(nomes)

# Acessando um elemento da lista
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(len(nomes))


# Adicionando um elemento na lista - no final da lista
nomes.append('Maria')
print(nomes)

nomes[0] =  'José'
print(nomes)

# Adicionando um elemento na lista - em uma posição especifica
nomes.insert(0, 'Marcola')
print(nomes)

# Removendo um elemento da lista
nomes.pop()
print(nomes)

# Removendo um elemento pelo index
nomes.pop(0)

# Removendo um elemento pelo valor
nomes.remove('João')


# Como encontrar um elemento em um determinado index
print(nomes.index('Pedro'))



lista = [1, 3, 2, 4, 7, 6,]

# Ordenando uma lista
lista.sort()
print(lista)

# Ordenando uma lista de forma reversa
lista.sort(reverse=True)
print(lista)

# forma NÃO pythonica
for i in range(0, len(lista)):
    print(lista[i])

# forma pythonica
for i in lista:
    print(i)


# Usando enumerate
for i, v in enumerate(lista):
    print(i, v)


# Matriz - Listas dentro de listas

matriz = [
    [1, 2, 3],
    [4, 5, 6]

]

print(matriz[0][2])  # vai mostrar 3

# Iterando sobre matriz

for linha in matriz:
    for coluna in linha:
        print(coluna, end='')

print()

