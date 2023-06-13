# Armazenando arquivos Binários

# O Python permite que você armazene dados binários em um arquivo usando o módulo pickle.

import pickle

# Criando um arquivo binário
# open(nome, modo)

# Modos de abertura de arquivo
# rb -> Abre para leitura binária
# wb -> Abre para escrita binária
# xb -> Abre para escrita binária somente se o arquivo não existir
# ab -> Abre para escrita binária, adicionando o conteúdo ao final do arquivo
# +b -> Abre para o modo de atualização binária: leitura e escrita

# Criando um arquivo binário
arquivo = open('pessoas.bin', 'wb')

