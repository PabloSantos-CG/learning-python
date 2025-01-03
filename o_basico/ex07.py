#Closure
def mult(factor):
    def factor_degree(number):
        return number * factor
    return factor_degree

double = mult(2)
triple = mult(3)
quadruple = mult(4)

print(f'O dobro de {5} é {double(5)}')
print(f'O tríplo de {5} é {triple(5)}')
print(f'O quadrúplo de {5} é {quadruple(5)}')