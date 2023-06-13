# Lambada , São funções não nomeadas
# São usadas quando?
# Quando queremos passar uma função como parâmetro para outra função



x = lambda x : x * 2
print(x(2))

lista = [1, 2, 3]
dobro = map(lambda x : x * 2, lista)
print(list(dobro))

