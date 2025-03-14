# PyPDF2 para manipular arquivos PDF (PdfWriter)
# PyPDF2 para manipular arquivos PDF (PdfMerger)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# @@ -9,7 +9,7 @@
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'pasta_nova'

with open(PASTA_NOVA / f'page.pdf', 'wb') as arquivo:
    # arquivo.add_page(page)
    arquivo.write(arquivo)  # type: ignore
files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',
]
merger = PdfMerger()
for file in files:
    merger.append(file)  # type: ignore
merger.write(PASTA_NOVA / 'MERGED.pdf')  # type: ignore
merger.close()