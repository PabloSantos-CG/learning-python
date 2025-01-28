import math

def size_formatter(size_file: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    # Se o tamanho for menor ou igual a 0, 0B.
    if size_file <= 0:
        return "0B"
    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abbreviated_size = ("B", "KB", "MB", "GB", "TB", "PB")
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do size_file
    # com a base (1024 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    abreviation_size_index = int(math.log(size_file, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    exponent = base ** abreviation_size_index
    # Nosso tamanho final
    size_calculated = size_file / exponent
    # A abreviação que queremos
    type_size = abbreviated_size[abreviation_size_index]
    return f'{size_calculated:.2f} {type_size}'