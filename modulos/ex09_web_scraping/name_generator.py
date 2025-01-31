import os
from pathlib import Path
from datetime import datetime

JOB_FOLDER = Path(__file__).parent / "all_data"

def name_generator(path_file = JOB_FOLDER):
    index = len(os.listdir(path_file))
    str_date = datetime.now().strftime("%d-%m-%Y")
    if index < 10:
        return f'0{index}.job_{str_date}'
    return f'{index}.job_{str_date}'

