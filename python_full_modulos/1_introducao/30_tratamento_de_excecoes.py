
try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Divide por: '))
    print(n1 / n2)

except ValueError:
    print('Digite apenas números')

except ZeroDivisionError:
    print('Não é possível dividir por zero')

except Exception as erro:
    print('Erro desconhecido. Erro: {}'.format(erro))



# Capturando uma exceção:
try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Divide por: '))
    print(n1 / n2)
except Exception as e:
    print(e)