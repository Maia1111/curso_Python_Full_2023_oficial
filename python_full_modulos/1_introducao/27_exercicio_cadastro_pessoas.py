# Faça um programa que usuario possa cadastrar  n pessoas
# e cada pessoa tem nome, idade e altura

lista = []
cont = 1


while True:
    opcao = int(input(f'=======Digite======  \n  1 -> Cadastrar \n  2 -> Sair: \n'))

    if opcao == 2:
        break

    if opcao != 1:
        print('Opção invalida')
        continue

    nome = input(f'Digite o nome da pessoa {cont}: ')
    idade = int(input(f'Digite a idade da pessoa {cont}: '))
    altura = float(input(f'Digite a altura da pessoa {cont}: '))
    pessoa = {'nome': nome, 'idade': idade, 'altura': altura}

    lista.append(pessoa)
    cont += 1
    print('=====================================================')

for pessoa in lista:
    print(pessoa['nome'] , pessoa['idade'], pessoa['altura'])




# Criar chave que ainda não foi definidade em dicionário
pessoa = {'nome':'Jose', 'idade': '33', 'altura': 1.89}
pessoa['cep'] = '3333333'

# Utilizando update
pessoa.update({'rua': 'Rua 1', 'bairro': 'Centro'})
print(pessoa)


# Iterando em um dicionario
for chave in pessoa:
    print(chave, pessoa[chave])

# Iterando em um dicionario com items
for chave, valor in pessoa.items():
    print(chave, valor)

# Trazendo somente valores:
for valor in pessoa.values():
    print(valor)

# Trazendo somente chaves:
for chave in pessoa.keys():
    print(chave)
