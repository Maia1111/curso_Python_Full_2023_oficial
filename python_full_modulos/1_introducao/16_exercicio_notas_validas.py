# Escreva um programa que receba notas de um aluno (0 - 10), caso 
# a nota digitada esteja fora dessa intervalo peça o professor para digitar novamente
# até que o valor seja válido.


# Solution:

while True:
    nota = int(input("Digite uma nota de 0 a 10: "))
    if nota >= 0 and nota <= 10:
        print(f'A nota do aluno foi : {nota}')
        break
    else:
        print("Nota inválida, digite novamente.")
        continue

# Solution 2:
while True:
    nota = int(input("Digite uma nota de 0 a 10: "))
    if nota < 0 or nota > 10:
        print("Nota inválida, digite novamente.")
        continue
    else:
        print(f'A nota do aluno foi : {nota}')
        break

