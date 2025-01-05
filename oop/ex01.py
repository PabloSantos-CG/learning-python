import json


class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

people_one = People("Fulano", 22, "M")
people_two = People("Cicrano", 42, "F")
people_tree = People("Beltrano", 62, "INDEFINIDO")

collections_peoples_instances = [vars(people_one), vars(people_two), vars(people_tree)]

print(collections_peoples_instances)

with open("oop/data.json", "w+") as file:
    json.dump(collections_peoples_instances, file, ensure_ascii='utf8')
