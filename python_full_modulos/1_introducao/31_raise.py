# Levantamento de exceção 


def soma(n1, n2):
    if type(n1) is not int or type(n2) is not int:
        raise ValueError("A soma só podem ser com números inteiros. ")
    return n1 + n2


soma(1, 'r')