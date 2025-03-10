

lista_nums = [1,2,3,4,5,6,7,8,9]
add_index = [] 
# buscar_num = int(input('Informe um numero : '))
buscar_num = 9

def per_lista():
    for index_first, num_first in enumerate(lista_nums):
        for index_second, num_second in enumerate(lista_nums):
            somados = num_first + num_second

            if somados == buscar_num:
                add_index.append((index_first, index_second))
                break
            

per_lista()

if add_index:
    print(add_index)
else:
    print(" Numero não consta na lista!! ")


# outro = [
#     (a, c) for a, b in enumerate(lista_nums)
#     for c, d  in enumerate(lista_nums)
#     if b + d == buscar_num
#     ]

# problema de memoria, e problema de index 
# print(outro)