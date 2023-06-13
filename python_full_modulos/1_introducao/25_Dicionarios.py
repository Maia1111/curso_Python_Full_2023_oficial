# Estrutura de dados com dicionarios
# Utilizando chaves e valor 
# As chaves são os nomes das variáveis

# Criando um dicionario vazio
dicionario = {}

dicionario = {'nome': 'Caio Sampaio', 'idade':'21', 'cep': '78888888'}
print(dicionario)


# Acessando um valor do dicionario
print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['cep'])

# Se voce tentar acessar uma chave que não existe, vai dar um KeyError 
# print(dicionario['rua'])

# Alterando um dicionario pela chave
dicionario['nome'] = 'Jose Souza'
print(dicionario)