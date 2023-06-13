# Conjuntos em Python
# Set 

# Listas aceita valores repetidos
x = [1, 2, 2, 3, 3, 4, 4, ]
print(x)

# Conjuntos não aceita valores repetidos
# Convertendo para conjunto a lista
x = set(x)
print(x)


# Unindo um conjunto com outro
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
t = x.union(y)
print(t)

# Intersecção de conjuntos
# tudo que contém em ambos os conjuntos
t = x.intersection(y)
print(t)

# Diferença de conjuntos
# tudo que contém em x e não contém em y
t = x.difference(y)
print(t)


# Diferença simétrica
# tudo que contém em x e não contém em y e vice versa
t = x.symmetric_difference(y)
print(t)