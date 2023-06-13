
with open('pessoas2.txt', 'w') as arq:
    arq.write('Nome: João idade: 20 \n')
    arq.write('Nome: Maria idade: 30 \n')
    arq.write('Nome: José idade: 40 \n')


with open('pessoas2.txt', 'r') as arq:
    resultados = arq.readlines()
    print(resultados)

