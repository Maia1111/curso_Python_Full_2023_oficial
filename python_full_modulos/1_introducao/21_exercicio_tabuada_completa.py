# Mostre a tabuada completa de todos os numeros entre 1 e 10

while True:
    n1 = int(input("De onde quer começar a tabuada: "))
    n2 = int(input("Até onde quer ir: "))
    n2 = n2 + 1
    if n1 < n2:
        break
    print("O primeiro digito não pode ser maior que o segundo!")
    print('===================================================')
    
    
  

for i in range(n1, n2):
    print(f'====================')
    for j in range(1, 11):
        print (f'{i} X {j} = {i * j}')