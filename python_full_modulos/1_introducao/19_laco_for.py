# Laço for

# Incrementando de 1 em 1
for i in range(0, 10):
    print(f'{i}')

# Incrementando de 2 em 2
for i in range(0, 100, 2):
    print(i)

# Decrementando de 1 em 1
print('==================================')

for i in range(11, 0, -1):
    print(i)


x = [2, 7, 'x', 'z', 45]

for i in x:
    print(f"{i}")



# Exemplo um pouco mais complexo - for aninhado
for i in range(0, 10):
    for j in range(0, 10):
        print(f'{i} {j} ')