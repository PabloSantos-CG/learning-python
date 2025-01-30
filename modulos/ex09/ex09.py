import requests, os
from pathlib import Path
from bs4 import BeautifulSoup, Tag
from typing import List, TypedDict
from copy import deepcopy
from ex09_errors import BadRequest, NotElement

# "https://portfolio-jet-ten-16.vercel.app/"
# "https://www.ba.gov.br/trabalho/280/vagas-do-dia-sinebahia"

# html = """
# <p>TRABALHADOR DA AGRICULTURA DEFENSIVO AGRICOLA <br/>Ensino Fundamental completo<br/>Experiência mínima de 06 meses na função<br/>Disponibilidade para morar na fazenda<br/>A empresa fornecerá alojamento, assistência médica, seguro de vida, auxílio mobilidade, PPR e refeição local. <br/>01 VAGA</p>
# """

url = "https://www.ba.gov.br/trabalho/280/vagas-do-dia-sinebahia"
response = requests.get(url)

if response.status_code != 200:
    raise BadRequest

soup = BeautifulSoup(response.text, "html.parser")

class JobObject(TypedDict):
    localizacao: str
    vagas: List[List[str]]

data_job: List[JobObject] = []
container = soup.select_one("#page-main > div > div.row.g-0 > div > div > article > div > div")

if not container:
    raise NotElement

permission = False
obj: JobObject = dict(localizacao="", vagas=[])
title_aux = None

for element in container.find_all(recursive=False):
    if not isinstance(element, Tag):
        continue

    if element.name == "h2" and permission == False:
        permission = True
    elif not permission:
        continue

    if element.name == "h2" and obj["localizacao"] == title_aux:
        data_job.append(deepcopy(obj))
        obj["localizacao"] = ""
        obj["vagas"] = []

    content = [tag.strip() for tag in element.stripped_strings]

    if not content:
        continue

    if len(content) == 1:
        obj["localizacao"], = deepcopy(content)
        title_aux = deepcopy(obj["localizacao"])
    else:
        obj["vagas"].append(deepcopy(content))


# [
#     {
#         "local": ...,
#         "lista de vagas desse local": ...
#     },
#     {
#         "local": ...,
#         "lista de vagas desse local": ...
#     },
#     ...
# ]
# criar um bloco de notas e a cada local dar um espaçamento maior


JOB_LIST = Path(__file__).parent / "data_jobs.txt"

with open(JOB_LIST, "a", encoding="utf8") as file:
    has_text = os.path.exists(JOB_LIST) and os.path.getsize(JOB_LIST) > 0
    if has_text:
        file.write("\n")

    for data in data_job:
        file.write(f'Local: {data["localizacao"]}\n')
        for job in data["vagas"]:
            for details in job:
                file.write(f'-\t{details}\n')
            file.write("\n")
