def add_repr_in_class(cls):
    def repr_difined(self):
        class_name = self.__class__.__name__
        class_repr = self.__dict__
        return f'{class_name}: {class_repr}'

    cls.__repr__ = repr_difined
    return cls


@add_repr_in_class
class Dog:
    def __init__(self, name, age_of_dog):
        self.name = name
        self.age = age_of_dog


@add_repr_in_class
class Cat:
    def __init__(self, name, age_of_cat):
        self.name = name
        self.age = age_of_cat

# Dog = add_repr_in_class(Dog)
# Cat = add_repr_in_class(Cat)

caramelo = Dog("Caramelo", 2)
planeta_osorio = Cat("Planeta Osório", 7)

print(caramelo)
print(planeta_osorio)