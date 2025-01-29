from pathlib import Path
import pprint
import requests
from bs4 import BeautifulSoup, Tag
from typing import List, TypedDict
from copy import copy

# "https://portfolio-jet-ten-16.vercel.app/"
# "https://www.ba.gov.br/trabalho/280/vagas-do-dia-sinebahia"

# html = """
# <p>TRABALHADOR DA AGRICULTURA DEFENSIVO AGRICOLA <br/>Ensino Fundamental completo<br/>Experiência mínima de 06 meses na função<br/>Disponibilidade para morar na fazenda<br/>A empresa fornecerá alojamento, assistência médica, seguro de vida, auxílio mobilidade, PPR e refeição local. <br/>01 VAGA</p>
# """

url = "https://www.ba.gov.br/trabalho/280/vagas-do-dia-sinebahia"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
data_list = []

container = soup.select_one("#page-main > div > div.row.g-0 > div > div > article > div > div")
permission = False

class Jobs(TypedDict):
    localizacao: str
    vagas: List[Tag]

obj: Jobs = {
    "localizacao": "",
    "vagas": []
}
title_aux = ""

# Problema -> repetindo o nome da localização sempre
for element in container.find_all(recursive=False):
    if not isinstance(element, Tag):
        continue

    if element.name == "h2" and permission == False:
        permission = True
    elif not permission:
        continue

    if element.name == "h2" and obj["localizacao"] == title_aux:
        data_list.append(obj)
        obj["localizacao"] = ""
        obj["vagas"] = []

    content = [tag.strip() for tag in element.stripped_strings]

    if len(content) == 1:
        obj["localizacao"], = content
        title_aux = copy(obj["localizacao"])
    else:
        obj["vagas"].append(content)




pprint.pprint(data_list)

# PATH_JSON = Path(__file__).parent / "data_jobs.txt"
# incrementar a busca e armazenamento em um json ou txt
