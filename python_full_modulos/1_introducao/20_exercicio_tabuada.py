# Receba um número e mostra a tabuada completa dele usando laço for

n1 = int(input("Digite um número que queira saber a tabuada: "))
for i in range(1, 11):
    print(f'{n1} X {i} = {n1 * i}')

