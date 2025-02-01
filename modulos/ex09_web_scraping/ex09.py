import requests
from pathlib import Path
from bs4 import BeautifulSoup, Tag
from typing import List, TypedDict
from copy import deepcopy
from ex09_errors import BadRequest, NotElement
from name_generator import name_generator

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
    local: str
    vagas: List[List[str]]


data_job: List[JobObject] = []
div_selector = "#page-main > div > div.row.g-0 > div > div > article > div > div"
container = soup.select_one(div_selector)

if not container:
    raise NotElement

permission = False
obj_aux: JobObject = dict(local="", vagas=[])
title_aux = None

for element in container.find_all(recursive=False):
    if not isinstance(element, Tag):
        continue

    if element.name == "h2" and permission == False:
        permission = True
    elif not permission:
        continue

    if element.name == "h2" and obj_aux["local"] == title_aux:
        data_job.append(deepcopy(obj_aux))
        obj_aux["local"] = ""
        obj_aux["vagas"] = []

    content = [tag.strip() for tag in element.stripped_strings]

    if not content:
        continue

    if len(content) == 1:
        obj_aux["local"], = deepcopy(content)
        title_aux = deepcopy(obj_aux["local"])
    else:
        obj_aux["vagas"].append(deepcopy(content))
data_job.append(deepcopy(obj_aux))

ORIGIN = Path(__file__).parent

# os.makedirs(ORIGIN / "all_data", exist_ok=True)
# os.makedirs(ORIGIN / "tech_data", exist_ok=True)

file_name = name_generator()

PATH_ALL_JOBS = ORIGIN / "all_data" / f"{file_name}.txt"
PATH_TECH_JOBS = ORIGIN / "tech_data" / f"{file_name}.txt"

data_tech_job: List[JobObject] = []

with open(PATH_ALL_JOBS, "a", encoding="utf8") as file:
    lines_all_jobs = []

    for data in data_job:
        lines_all_jobs.append(f'Local: {data["local"]}\n')
        for job in data["vagas"]:
            if any("PCD" in detail.upper() for detail in job):
                continue

            for detail in job:
                lines_all_jobs.append(f'-\t{detail}\n')

            has_tech_key = any("TECNOLOGIA" in detail.upper() for detail in job)
            if has_tech_key:
                data_tech_job.append({"local": data["local"], "vaga": job})
            lines_all_jobs.append("\n")
    file.writelines(lines_all_jobs)


with open(PATH_TECH_JOBS, "a", encoding="utf8") as file:
    lines_tech_jobs = []

    for obj_tech in data_tech_job:
        lines_tech_jobs.append(f'Local: {obj_tech["local"]}\n')
        for details_vacancy in obj_tech["vaga"]:
            lines_tech_jobs.append(f'-\t{details_vacancy}\n')
    file.writelines(lines_tech_jobs)
