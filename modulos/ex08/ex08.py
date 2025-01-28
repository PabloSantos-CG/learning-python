"""
criar uma pasta
criar 10 arquivos dentro dessa pasta
"""
import os, shutil
from pathlib import Path
from zipfile import ZipFile

PATH_FOLDER = Path(__file__).parent / "FILES"
PATH_ZIP = PATH_FOLDER.parent / "FILES.zip"

def create_files(qtd: int):
    shutil.rmtree(PATH_FOLDER, ignore_errors=True)
    os.makedirs(PATH_FOLDER)

    for i in range(qtd):
        path_ = PATH_FOLDER / f'arquivo{i}.txt'
        with open(path_, "w") as file:
            file.write(f'arquivo{i}.txt')
create_files(10)

def create_zip():
    Path.unlink(PATH_ZIP, missing_ok=True)

    with ZipFile(PATH_ZIP, "w") as zip:
        for root, dirs, files in os.walk(PATH_FOLDER):
            for file in files:
                zip.write(os.path.join(root, file), file)
create_zip()

#outros

# -> Lendo arquivos de um zip

# with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
#     for arquivo in zip.namelist():
#         print(arquivo)


# -> Extraindo arquivos de um zip

# with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
#     zip.extractall(CAMINHO_DESCOMPACTADO)