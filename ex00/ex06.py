try:
    CPF = input("Informe seu CPF: ")\
    .replace(".", "").replace("-", "").replace(" ", "")

    if len(CPF) != 11:
        print("O CPF deve conter 11 dígitos válidos.")
    else:
        first_factor = 10
        last_factor = 11
        first_accumulator = 0
        last_accumulator = 0

        for i, digit in enumerate(CPF):
            if i == 9:
                last_accumulator += int(CPF[-2]) * last_factor
                break

            last_accumulator += int(digit) * last_factor
            last_factor -= 1

            first_accumulator += int(digit) * first_factor
            first_factor -= 1

        first_accumulator = (first_accumulator * 10) % 11
        last_accumulator = (last_accumulator * 10) % 11
        first_digit = first_accumulator if first_accumulator <= 9 else 0
        last_digit = last_accumulator if last_accumulator <= 9 else 0

        if first_digit == int(CPF[-2]) and last_digit == int(CPF[-1]):
            print("O CPF é Válido!")
        else:
            print("O CPF que você informou é inválido.")

except ValueError:
    print("Os dígitos do cpf devem ser valores numéricos.")