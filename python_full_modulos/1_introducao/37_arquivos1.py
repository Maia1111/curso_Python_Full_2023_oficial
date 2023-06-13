#ARQUIVOS
# Arquivos são usados para persistir dados
# Arquivos são usados para armazenar dados de forma permanente  


# Criando um arquivo
# open(nome, modo)

# Modos de abertura de arquivo
# r -> Abre para leitura - padrão
# w -> Abre para escrita - sobrescreve caso o arquivo já exista
# x -> Abre para escrita somente se o arquivo não existir
# a -> Abre para escrita, adicionando o conteúdo ao final do arquivo
# + -> Abre para o modo de atualização: leitura e escrita


arquivo = open('pessoas.txt', 'a')


i = 0 

while i < 2:
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    arquivo.write(f'Nome: {nome} idade: {idade} \n')
    i += 1


arquivo = open('pessoas.txt', 'r')

resultados = arquivo.readlines()

print(resultados)

for i in resultados:
    print(i)