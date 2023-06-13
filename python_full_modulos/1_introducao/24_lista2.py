# Receba 10 valores e exiba a soma de todos os eles 

lista = []
soma = 0

for i in range(0,10):
    lista.append(int(input('Digite um valor: ')))
    
for i in lista:
    soma += i
print('A soma dos valores é: ', soma)


# Utilizando list compreension 
lista  = [int(input("Digite um numero: ")) for i in range(0, 10)]
print(sum(lista))


# List Compreension dentro de lista
x = [[ j for j in range(0, 4)] for i in range(0, 4)]
print(x)


# list Compreension com condicionais
x = [i for i in range(0, 10) if i % 2 == 0]
print(x)




