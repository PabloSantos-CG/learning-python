class SerVivo:
    #atributo de classe, ao modificar diretamente os atributos de classe, modificamos os atributos de classe que pertende à instâncias
    come = True
    respira =True
    dorme = True


class Pessoa(SerVivo):
    def __init__(self, nome, idade):
        #atributo de instância
        self.nome = nome
        self.idade = idade

    @property
    def show(self):
        return [self.__dict__, {'come': self.come, 'dorme': self.dorme, 'respira': self.respira}]


class Cliente(Pessoa):
    def __init__(self, usuario):
        self.usuario = usuario

    @property
    def show(self):
        return ['MRO - Method Resolution Order', super().show]


fulano = Pessoa('Fulano', 22)
print(*fulano.show, sep='\n')

cliente = Cliente("cicrano")
print(*cliente.show, sep='\n')