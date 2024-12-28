name_input = input("Informe seu nome: ")
age_input = input("Informe sua idade: ")
name_validated = name_input.split() and name_input.isalpha()

if name_validated and age_input.isdigit():
    age = int(age_input)
    name_length = len(name_input)
    name_inverted = name_input[-1:: -1]
    
    print(
        "Seu nome é: ", name_input,
        "\nSeu nome invertido é: ", name_inverted,
        "\nSeu nome tem: ", name_length, " letras",
        "\nA primeira letra do seu nome é: ", name_input[0],
        "\nA última letra do seu nome é: ", name_input[name_length-1]
    )
else:
    print("\nTente novamente.")