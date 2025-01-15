from typing import Literal
from oop.ex09.ex09_account import SavingsAccount, CheckingAccount


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (
            f'Nome: {self.name}; Idade: {self.age}'
        )


TypeUserAccount = Literal["poupança", "conta-corrente"]

class Client(People):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.__account = None

    @property
    def account(self):
        return self.__account

    def __validate_type_account(self, type_account: str):
        is_invalid = (False, "Operação inválida!")
        if not type_account.isalpha():
            return is_invalid

        type_account = type_account.strip().lower()
        if type_account == "poupanca" or type_account == "poupança":
            return (True, "poupança")
        elif type_account == "conta-corrente" or type_account == "conta corrente":
            return (True, "conta-corrente")
        else:
            return is_invalid

    def set_account(self, agency: str, number_account: str, type_account: TypeUserAccount):
        if self.account is not None:
            return (False, 'A conta já foi definida!')

        type_account_validated = self.__validate_type_account(type_account)

        if type_account_validated[1] == "poupança":
            self.__account = SavingsAccount(agency, number_account)
            return (True, 'Você criou uma conta poupança.')
        elif type_account_validated[1] == "conta-corrente":
            self.__account = CheckingAccount(agency, number_account)
            return (True, 'Você criou uma conta-corrente.')
        return type_account_validated

    def __str__(self):
        string_ = '\"Cliente ainda não definiu uma conta\"'
        return (
            f'\n{super().__str__()}'
            f'\nConta do usuário: {
                self.account
                if self.account is not None else string_
            }'
            f'\n'
        )

if __name__ == "__main__":
    fulano = Client("Fulano", 22)
    
    print(fulano)
    fulano.set_account("0001", "00000-1", "conta-corrente")
    
    print()