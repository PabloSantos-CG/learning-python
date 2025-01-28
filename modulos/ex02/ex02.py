def take_out_loan(loan_amount: float):
    from datetime import datetime

    if not isinstance(loan_amount, (int, float)):
        return False

    # loan_amount  = 1000

    contract_duration_in_years = 5
    total_installments = contract_duration_in_years * 12
    installments_value = round((loan_amount/ total_installments), 2)

    prompt_ = "20/12/2020"

    initial_date = datetime.strptime(prompt_, "%d/%m/%Y")
    end_date = initial_date.replace(year= initial_date.year + contract_duration_in_years)

    def date_formatter(date: datetime):
        if date.month == 12:
            return date.replace(day=20, month=1, year= date.year + 1)
        elif date.day != 20:
            return date.replace(day=20)
        return date

    def change_month(date: datetime):
        if date.month == 12:
            return date_formatter(date)
        return date.replace(month= date.month + 1)

    tickets_list = []
    copy_datetime = initial_date
    for i in range(1, (total_installments+1)):
        if i == 1 and copy_datetime.month == 12:
            copy_datetime = date_formatter(copy_datetime)

        ticket = {
            "Boleto": f'Nº {i}',
            "Data de vencimento da parcela": copy_datetime.strftime("%d/%m/%Y"),
            "Valor": installments_value,
        }

        copy_datetime = change_month(copy_datetime)
        tickets_list.append(ticket)

    return {
        "Início do contrato": initial_date.strftime("%d/%m/%Y"),
        "Vencimento do contrato": end_date.strftime("%d/%m/%Y"),
        "Boletos": tickets_list
    }

t_list = take_out_loan(9000)
print("Início do contrato:", t_list["Início do contrato"])
print("Vencimento do contrato:", t_list["Vencimento do contrato"])
print("Boletos:")
for boleto in t_list["Boletos"]:
    print(boleto)
