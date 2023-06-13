# Operadores aritiméticos
# + - * / ** % // mat.sqrt

import math

# Precedência
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -

operacoes = 2 + 2   # Adição 
operacao2 = 2 - 2
operacao3 = 2 * 2
operacao4 = 2 / 2
operacao5 = 2 ** 2
operacao6 = 2 % 2  
operacao7 = 2 // 2


raiz = int(input("Digite o numero que quer a raiz quadrada: "))
raiz = raiz ** 0.5
print(raiz)

# utilizando math 
raiz = math.sqrt(10)
print(raiz)