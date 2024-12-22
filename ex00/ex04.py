import os

word = "PANELA"
word_encripted = "*" * len(word)
word_erros = 0

while True:
    os.system("cls")
    if word_encripted == word:
        print("\n\nParabéns você adivinhou a palavra! :) \nSaindo...")
        break

    print(f'{"-"*50}\
        \nSeja Bem-Vindo(a) ao "adivinha se puder".\
        \nPalavra: {word_encripted}\
        \nTentativas erradas: {word_erros}\
    \n\n{"-"*50}')

    letter = input("Informe uma letra: ").upper()
    if letter.isalpha() and len(letter) == 1:
        if letter in word_encripted:
            print("Letra repetida, tente novamente.")
            word_erros += 1
        elif letter in word:
            aux = ""
            for i in range(len(word)):
                if word[i] == letter:
                    aux += word[i]
                else:
                    aux += word_encripted[i]
            word_encripted = aux

            print("\nParabéns! Você acertou.")
        else:
            word_erros+=1
    else:
        print("\nLetra inválida! Tente informar uma letra de A-Z.")


    pedido_de_saida = input("\nDeseja continuar tentando? \nDigite 'x'(para continuar) ou 's'(para sair): ").lower()
    if pedido_de_saida == "s":
        break
    elif pedido_de_saida == "x":
        continue
    else:
        print("\nComando inválido! \nDigite 's' para sair ou 'x' para continuar.")

print(f'{"-"*50}\
        \nObrigado por jogar.\
        \nPalavra era: {word}\
        \nTentativas erradas: {word_erros}\
    \n\n{"-"*50}')