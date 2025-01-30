class BadRequest(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = "Houve um erro de requisição"

class NotElement(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = "Houve um erro ao procurar pelo elemento e 'None' foi retornado"