class MultiplicatorManufacture:
    def __init__(self, multiplicator):
        self.multiplicator = multiplicator

#call permite usar a instância como se fosse uma função
#callable
    def __call__(self, factor):
        return self.multiplicator * factor

double = MultiplicatorManufacture(2)
print(double(8))


class ClassAsDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Iniciou com decorator")
        return self.func(*args, **kwargs)

@ClassAsDecorator
def calc(a,b):
    return a + b

print(calc(2, 2))