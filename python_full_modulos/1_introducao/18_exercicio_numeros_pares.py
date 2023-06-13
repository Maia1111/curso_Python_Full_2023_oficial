# Recebe a um numero e mostre todos os números pares de  0 até o número digitado

# Solution:
n1 = int(input('Digite um numero: '))

i = 1
while i <= n1:
    if i % 2 == 0:
        print(i)
    i += 1
