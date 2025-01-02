import json
import os

def todo():
    todo_list = []
    mirror = []

    while True:
        user_input = input(f'\nQuantidade de elementos na lista: {len(todo_list)} \n\nO que deseja adicionar ? ').lower()

        if user_input == "clear":
            os.system("cls")
        elif not user_input.isalpha():
            print(f'Inválido! {"-"*50}')
        elif user_input == "sair":
            print("\nSaindo...")
            return todo_list
        elif user_input == "listar":
            if len(todo_list) == 0:
                print("\nNão há elementos na lista!\n")
                continue

            for value in todo_list:
                print(f'\t- {value}')
        elif user_input == "desfazer":
            if len(user_input) == 0:
                print("\nNão há o que apagar!\n")
                continue
            mirror.append(todo_list.pop())
        elif user_input == "refazer":
            if len(mirror) == 0:
                print("\nNão há o que refazer!\n")
                continue
            todo_list.append(mirror.pop())
        elif user_input in todo_list:
            print("\nElemento repetido!\n")
        else:
            todo_list.append(user_input)

def execute():
    data = todo()
    with open("data.json", "w+", encoding="utf8") as file:
        json.dump(data, file)

execute()