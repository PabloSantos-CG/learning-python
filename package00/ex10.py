from itertools import zip_longest
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))

# -> Zip: permite unir duas lista com base na de menor índice, devolvendo uma lista de tuplas
# -> Zip_longest: faz a mesma coisa, mas usa a lista de maior índice como base
