def create_list(value, new_list: list =[]):
    new_list.append(value)
    return new_list

var1 = create_list(True)
create_list('2', var1)

var2 = create_list('lorem ipsum dollor')
create_list('4', var2)

var3 = create_list('alguma', [])
create_list('coisa', var3)

print('\nvalor', var1)
print('id', id(var1))

print('\n\nvalor', var2)
print('id', id(var2))

print('\n\nvalor', var3)
print('id', id(var3))
#problema com parâmetros mutáveis + valor padrão