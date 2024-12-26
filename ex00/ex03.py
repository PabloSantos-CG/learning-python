# number_input = input("Digite um número inteiro: ")

# if number_input.isdigit():
#     int_number = int(number_input)

#     if int_number % 2 == 0:
#         print("Este número é par.")
#     else:
#         print("Este número é ímpar.")
# else:
#     print("Você deve informar um número inteiro.")

####

# try:
#     hour_input = input("Informe o horário: ")
#     hour = int(hour_input)
    
#     if hour >= 0 and hour <= 11:
#         print("Bom dia.")
#     elif hour >= 12 and hour <= 17:
#         print("Boa tarde.")
#     elif hour >= 18 and hour <= 23:
#         print("Boa noite.")
#     else:
#         print("404 ;)")

# except:
#     print("Você deve informar o horário em números válidos.")


####

name_input = input("Informe seu nome: ")

if name_input.isalpha():
    name = name_input.strip()
    
    if len(name) <= 4:
        print("Seu nome é curto.")
    elif len(name) >= 5 and len(name) <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")
else:
    print("Nome inválido! Tente novamente.")