# Exercicio o programa vai dizer qual numero maio dos digitados

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

print(f'Voce digitou os numeros {numero1}, {numero2}, {numero3}')

if numero1 > numero2 and numero1 > numero3:
    print(f'o numero {numero1} é o maior')
elif numero2 > numero1 and numero2 > numero3:
    print(f'o numero {numero2} é o maior')
else:
    print(f'o numero {numero3} é o maior')