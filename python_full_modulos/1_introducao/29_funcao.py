# Funções em Python é um estrututa que por ou não receber algum valor
# Processar 
# Retornar ou não algum valor

def minha_funcao():
    print('Oi')
    print('tudo bem ? ')

# mostra o endereço de memoria da função 
print(minha_funcao)

# Executa a função
minha_funcao()


# você pode chamar uma função quantas vezes quizer 

print('=============================================================')

# funções com parametros de entrada
# Quando você esta criando um função oque esta dentro das chaves são parâmetros 
# Quando você esta chamando uma função oque esta dentro das chaves são argumentos

def soma(x, y):
    print(x + y)

soma(2, 3)
soma(4, 5)


# E quando eu quero receber varios valores 
# Eu utilizo o *args
def minha_funcao2(*args):
    print(sum(args))


# Executanto a função com args
minha_funcao2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Utilizando kwargs
# Quando você quer receber um dicionario como parametro de entrada

def minha_funcao3(**kwargs):
    print(kwargs)

minha_funcao3(nome='Caio', idade=22, altura=173)



def argumentos(**kwargs):
    x = kwargs.get('teste4')
    if x:
        print('Existe')
    else:
        print('Não existe')


# Testeando a função com argumento que existe
argumentos(teste1=1, teste2=2, teste3=3, teste4=4)

# Testeando a função com argumento que não existe
argumentos()


# Funções com retorno
# Quando você quer que a função retorne um valor

def soma(x, y):
    return x + y

resultado = soma(1, 2)
print(resultado)