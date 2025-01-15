""""
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)

Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    -> Checar se a agência é daquele banco
    -> Checar se o cliente é daquele banco
    -> Checar se a conta é daquele banco

Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from itertools import zip_longest
from ex09_client import Client, TypeUserAccount

class Bank:
    def __init__(self, name: str, agency: str):
        self._name = name
        self._agency = agency
        self.__clients: list[Client] | list = []
        self.__accounts = []

    @property
    def name(self):
        return self._name

    @property
    def agency(self):
        return self._agency

    def __already_exists(self, number_account: str, type_account: TypeUserAccount) -> bool:
        if len(self.__clients) == 0:
            return False

        for client in self.__clients:
            label_account_is_equal = client.account.label == type_account
            number_account_is_equal = client.account.number_account == number_account
            if label_account_is_equal and number_account_is_equal:
                return True
            return False

#   implementar a separação da criação de cliente
    # def __validate_creation(self):
    #     ...

    def create_new_client(self, name: str, age: int, number_account: str, type_account: TypeUserAccount):
        unsuccessful = { "status_success": False, "new_client": None }

        if not isinstance(name, str) or not name.isalpha():
            return  {**unsuccessful, "details": "A propriedade 'name' deve ser string"}
        elif not isinstance(age, int) or not number_account.isdigit():
            return  {**unsuccessful, "details": "Tipo inválido"}

        exists = self.__already_exists(number_account, type_account)
        if exists:
            return {**unsuccessful, "details": "Cliente já existe"}

        new_client = Client(name, age)
        result_account_creation = new_client.set_account(self._agency, number_account, type_account)
        if result_account_creation[0] is False:
            return {**unsuccessful, "details": result_account_creation[1]}

        self.__clients.append(new_client)
        self.__accounts.append(new_client.account)

        return { "status_success": True, "new_client": new_client, "details": "Conta criada" }

    def __validate_operations(self, number_account: str, type_account: TypeUserAccount):
        label_account = ["poupanca", "poupança", "conta-corrente", "conta corrente"]
        if not number_account.isdigit() or not type_account in label_account:
            return False

        result = next(
            (index, client) for index, client in enumerate(self.__clients)
            if (client.account.number_account == number_account and
                client.account.label == type_account)
        )
        return result

    def make_deposit(self, value: int | float, number_account: str, type_account: TypeUserAccount):
        is_client = self.__validate_operations(value, number_account, type_account)

        if not is_client:
            return (False, "Não é cliente")
        return is_client[1].account.deposit(value)

    def make_withdrawal(self, value: int | float, number_account: str, type_account: TypeUserAccount):
        is_client = self.__validate_operations(value, number_account, type_account)

        if not is_client:
            return (False, "Não é cliente")
        return is_client[1].account.withdraw(value)

    def show_clients(self):
        clients_in_string = "Clientes: \n"

        if len(self.__clients) == 0:
            clients_in_string += "Não há clientes cadastrados ainda"
            return clients_in_string

        for client in self.__clients:
            clients_in_string += f'{client.__str__()}\n'
        return clients_in_string

    def show_accounts(self):
        accounts_in_string = "Contas: \n"

        if len(self.__accounts) == 0:
            accounts_in_string += "Não há contas cadastrados ainda"
            return accounts_in_string

        for account in self.__accounts:
            accounts_in_string += f'{account}\n'
        return accounts_in_string

    def __str__(self):
        clients_in_string = ""
        accounts_in_string = ""

        for clients, accounts in zip_longest(self.__clients, self.__accounts):
            if clients:
                clients_in_string += f'{clients}\n'
            if accounts:
                accounts_in_string += f'{accounts}\n'

        return(
            f'\nBanco: {self.name}'
            f'\nAgência: {self.agency}'
            f'\nClientes: \n{
                clients_in_string
                if len(self.__clients) != 0 else "Ainda não há clientes cadastrados."
            }'
            f'\nContas: \n{
                accounts_in_string
                if len(self.__accounts) != 0 else "Ainda não há contas cadastradas."
            }'
        )

caixa_economica = Bank("Caixa-Econômica", "0001")
bradesco = Bank("Bradesco", "0002")
itau = Bank("Itaú", "0003")

# print(caixa_economica)
# print("~//~"*25)

# print(bradesco)
# print("~//~"*25)

# print(itau)
# print("~//~"*25)

fulano_caixa_economica = caixa_economica.create_new_client("Fulano", 22, "010101", "poupança")
caixa_economica.create_new_client("Cicrano", 22,"020202","conta-corrente")

print(caixa_economica)

# print(caixa_economica.show_clients())
# print(caixa_economica.show_accounts())