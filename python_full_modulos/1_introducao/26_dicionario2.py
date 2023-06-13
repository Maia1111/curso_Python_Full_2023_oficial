# Dicionarios 2

x = {'nomes': []}

for i in range(0, 3):
    x['nomes'].append(input("Digite um nome: "))

print(x['nomes'] [0])


pessoas = [{'nome': 'Caio', 'idade': '22', 'altura': 173}, 
           {'nome': 'Jose', 'idade': '21', 'altura': 170},
           {'nome': 'Maria', 'idade': '20', 'altura': 160}]


for pessoa in pessoas:
    print(pessoa['nome'], pessoa['idade'], pessoa['altura'])