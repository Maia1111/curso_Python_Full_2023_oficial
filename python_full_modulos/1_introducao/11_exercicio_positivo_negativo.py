# Exercicio mostrar se o número é positivo ou negativo

numero = float(input("Digite um numero: "))
if numero > 0:
    print(f'O numero {numero} é positivo')
elif numero < 0:
   print(f'O numero {numero} é negativo')
else:
    print(f'O numero {numero} é neutro')
    