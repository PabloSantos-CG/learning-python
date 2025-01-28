import locale
from string import Template
from datetime import datetime
from pathlib import Path

PATH_FILE = Path(__file__).parent / "ex06.txt"

locale.setlocale(locale.LC_ALL, '')

def convertter_brl(value: float) -> str:
    brl = 'R$ ' + locale.currency(value, symbol=False, grouping=True)
    return brl

date = datetime(2022, 12, 28)
person = dict(
    name='Marta Doe',
    value= convertter_brl(1_234_456),
    date= date.strftime('%d/%m/%Y'),
    enterprise='Jhon Doe',
    phone='+55 (11) 9999-5432',
)

# result: str

with open(PATH_FILE, "r", encoding="utf8") as file:
    text_file = file.read()
    result = Template(text_file).substitute(person)
    # result = Template.substitute(text_file, person)

print(result)
