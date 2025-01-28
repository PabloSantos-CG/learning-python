import os
from modulos.ex03.ex03_02 import size_formatter


path_main = os.path.join("\\Users", "aspir", "Desktop")

for root, dirs, files in os.walk(path_main):
    print('Caminho atual: ', root)

    for dir_ in dirs:
        print('Pasta: ', dir_)

    for f in files:
        size = os.path.getsize(os.path.join(root, f))
        size_formatted = size_formatter(size)
        print(f'Arquivo: {f}  {size_formatted}')

    # for f in files:
    #     name_file, extension_file = os.path.splitext(f)
    #     if name_file == "ideia_de_projeto":
    #         with open(os.path.join(root, f), "r", encoding="utf8") as file:
    #             print(file.read())

    print()
    