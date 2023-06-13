# Receba uma temperatura em Farenheit e exiba em graus celsius

# c = 5 * f - 32 / 9 

temperatura_farenheit = float(input("Digite a temperatura em graus farenheit: "))

temperatura_celsius = 5 * ((temperatura_farenheit - 32) / 9)

temperatura_celsius = round(temperatura_celsius, 2)
print(f'A temperatura em graus celsius é : {temperatura_celsius}')

