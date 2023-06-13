# Estrututura de decisão 
# A estrutura de decisão é utilizada para decidir se um bloco de instruções será executado ou não, dependendo de uma condição.
nota1 = float(input("Qual foi a nota 1 do aluno: "))
nota2 = float(input("Qual foi a nota 2 do aluno: "))
nota3 = float(input("Qual foi a nota 3 do aluno: "))
media = (nota1 + nota2 + nota3) / 3


if media >= 6:
    if media < 7:
        print(f'APROVADO, média {media}, muito bom, mas você pode ser melhor!')
    elif media < 8:
        print(f"APROVADO, média {media}, sua nota foi boa!")
    else:
        print(f"APROVADO, média {media}, sua nota foi excelente!")

elif media >= 4 and media < 6.5:
    print(f'RECUPERAÇÃO, média {media}')
else:
    print(f'REPROVADO, média {media}')
