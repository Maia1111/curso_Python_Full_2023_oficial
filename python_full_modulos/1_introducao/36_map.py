# Função MAP em Python faz oque?
# Map é uma função que recebe dois parâmetros:  
# Recebe uma função lambda normalmente e um iteravel
# Onde o primeiro parametro é o filtro que o iteravel vai receber
# Exemplo:

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = list(map(lambda n: n * 2, lista))
print(x)

# Passando uma lista de dicionários para função map

pessoas = [{'nome': 'Marcelo', 'idade': 22}, {'nome': 'Armando', 'idade': 44}, {'nome': 'jose', 'idade': 17}]
x = list(map(lambda pessoa:pessoa['idade'] > 22, pessoas))
print(x)