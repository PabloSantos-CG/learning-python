import os


shopping_list = []

while True:
    print(f'{"-"*50}\nItens na lista: {len(shopping_list)}\n')
    print("Opções: \n\t(1) Adicionar um item \n\t(2) Listar todos os itens \n\t(3) Apagar um item \n\t(s) Sair \n\t(c) Para limpar o terminal. \n")
    option = input("Informe sua opção: ")

    if option == "c":
        os.system("cls")
        continue
    elif len(option) != 1:
        print(f'{"-"*50}\nOpção inválida! Escolha UMA opção.')
        continue
    elif option.lower() == "s":
        print(f'{"-"*50}\nSaindo...')
        break

    if option == "1":
        item = input(f'{"-"*50}\nInforme o item a ser adicionado: ').upper()
        validation_item = item.replace(" ", "")

        if validation_item.isalpha():
            shopping_list.append(item)
            print(f'O item "{item}" foi adicionado à lista.')
        elif item.isalpha() and item in shopping_list:
            print(f'O item "{item}" já existe na lista, no índice "{shopping_list.index(item)}"')
        else:
            print(f'Item inválido!')

    elif option == "2":
        if len(shopping_list) == 0:
            print(f'{"-"*50}\nLista vazia.')
            continue

        print(f'{"-"*50}\nA lista contém:')
        for i, item in enumerate(shopping_list):
            print(f'{i} \tItem: {item}')

    elif option == "3":
        if len(shopping_list) == 0:
            print(f'{"-"*50}\nNão há itens para remover.')
            continue

        index_item = input("Informe o índice do elemento que deseja apagar: ")

        if not index_item.isnumeric():
            print("Índice inválido!")
            continue

        length_shopping_list = len(shopping_list) - 1
        index_item = int(index_item)

        if index_item == 0:
            item_removed = shopping_list.pop(int(index_item))
            print(f'O item "{item_removed}" foi removido da lista.')
        elif index_item > length_shopping_list or index_item < 0:
            print(f'Índice inválido!')
        else:
            item_removed = shopping_list.pop(int(index_item))
            print(f'O item "{item_removed}" foi removido da lista.')