from pathlib import Path


class MyContextManager:
    def __init__(self, path_file, mode):
        self.path_file = path_file
        self.mode = mode
        self._file = None

    def __enter__(self):
        self._file = open(self.path_file, self.mode, encoding='utf8')
        return self._file

    def __exit__(self, except_type, except_val, except_traceback):
        if except_type:
            return f'Tipo: {except_type}, valor: {except_val}, detalhe: {except_traceback}'
        print(f'Arquivo: {self._file}')
        self._file.close()

my_path = Path(__file__).parent / 'my_context_manager.txt'

with MyContextManager(my_path, "w+") as f:
    f.write('Hello World!')