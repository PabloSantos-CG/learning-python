from pathlib import Path
from openpyexcel import Workbook
from openpyexcel.worksheet.worksheet import Worksheet

ROOT_FOLDER = Path(__file__).parent
FILE_EXCEL = ROOT_FOLDER / "excel" / "file.xlsx"

workbook = Workbook()
worksheet: Worksheet = workbook.active

worksheet.cell(1, 1, "Nome")
worksheet.cell(1, 2, "Idade")
worksheet.cell(1, 3, "Nota")

students = [
    # nome      idade nota
    ['João',    14,   5.5],
    ['Maria',   13,   9.7],
    ['Luiz',    15,   8.8],
    ['Alberto', 16,   10],
]

workbook.save(FILE_EXCEL)