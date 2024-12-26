## Método print()
#sep='' -> separador entre argumentos
#end='' -> separador no final
# print("Olá", "mundo!", sep='Isso vai se repetir entre os argumentos', end='fim')

# \r \n -> CRLF 'serve para quebras de linhas no WINDOWS'
# \n -> LF 'quebra a linha no linux'

## Tipos primitivos e imutáveis em Python -> int, float, str e bool

##Casting(conversão de tipos) -> usamos os métodos bool() int() float() str()

## divisão que retorna float -> 2 / 2
## divisão que retorna int -> 2 // 2

#formatar casas decimais
# variavel = 5/3
# print(f'{variavel:.2f}')

# string_qualquer = "i am string"

# string_qualquer.format()


## ÍNDICES no Python:
#  0  1  2  3  4  <- índices
#  P  A  B  L  O 
# -5 -4 -3 -2 -1  <- índices negativos  (observer que '-1' é a última posição)

"""
INTERPOLAÇÃO DE STRINGS: usa-se '%'
    's'        -> string
    'd' e 'i'  -> int
    'f'        -> float
    'x' e 'X'  -> Hexadecimal (maiúsculo ou minúsculo)

(Caractere) e (quantidade)
    > -> Esquerda
    < -> Direita
    ^ -> Centro
    Conversion flags - !r !s !a 
"""

name = "ABC"


print(f'início {name: ^13} fim')

##FATIAMENTO EM STRINGS:
# [i:f:s] -> (início; fim; salto)
# se valor negativo, começa do final da string
