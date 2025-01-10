#conta
"""
conta-corrente / conta-poupança
- conta herda de banco
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
"""
from abc import ABC, abstractmethod
from enum import Enum

class CasesWhenCheckingBalance(Enum):
    INVALID_TYPE = (False, 'Tipo inválido')
    NO_BALANCE = (False, 'Não há saldo suficiente para completar a operação.')
    ZERO_OR_LESS = (False, 'Operação inválida! Informe um valor maior que zero.')
    NO_EXTRA_LIMIT = (False, 'Valor excede: (saldo + limite extra)')
    SUCCESS = (True, 'Solicitação válida!')


class Account(ABC):
    def __init__(self, agency: str, number_account: str):
        self._agency = agency
        self._number_account = number_account
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, value):
        if isinstance(value, (int, float)):
            self._balance += value

    @abstractmethod
    def withdraw(self, value: int | float):
        ...

    def validate_withdrawal_amount(self, value: int | float, balance_plus_limit= None):
        if not isinstance(value, (int, float)):
            return CasesWhenCheckingBalance.INVALID_TYPE.value

        if balance_plus_limit:
            if value > balance_plus_limit:
                return CasesWhenCheckingBalance.NO_EXTRA_LIMIT.value
            elif (value > 0 and value <= balance_plus_limit):
                return CasesWhenCheckingBalance.SUCCESS.value

        if value <= 0:
            return CasesWhenCheckingBalance.ZERO_OR_LESS.value
        elif value > self.balance:
            return CasesWhenCheckingBalance.NO_BALANCE.value

        return CasesWhenCheckingBalance.SUCCESS.value

    def __str__(self):
        return (
            f'\nAgência: {self._agency}; Conta: {self._number_account}'
            f'\nSaldo: {self.balance:.2f}'
        )


class SavingsAccount(Account):
    def __init__(self, agency, number_account):
        super().__init__(agency, number_account)

    def withdraw(self, value):
        checked = self.validate_withdrawal_amount(value)

        if not checked[0]:
            return checked
        self._balance -= value
        print(f'Você sacou: R$ -{value:.2f}')
        return checked


class CheckingAccount(Account):
    def __init__(self, agency, number_account):
        super().__init__(agency, number_account)
        self.__extra_limit = 300

    def withdraw(self, value):
        balance_plus_limit = self.balance + self.__extra_limit

        checked = self.validate_withdrawal_amount(value, balance_plus_limit)
        if not checked[0]:
            if checked[1] == CasesWhenCheckingBalance.NO_EXTRA_LIMIT.value:
                print(f'Limite extra: {self.__extra_limit}')
            return checked

        if value <= self.balance:
            self._balance -= value
            print(f'Você sacou: R$ -{value:.2f}')
            return checked

        request_balance_difference = value - self.balance
        # nesse ponto, quer dizer que eu tenho o valor no limite, se não tinha parado na validação de saldo
        required_value = self.__extra_limit - request_balance_difference
        self.__extra_limit -= required_value
        self._balance += required_value
#-> -> problema na lógica, saldo ta invertendo e virando a diferença(debug para ver) <- <-
        print(f'Valor plus: {balance_plus_limit} \nDiferença entre saldo e pedido: {request_balance_difference}')
        print(f'Valor necessário para completar a transação: {required_value}')
        print(f'Saldo após acréscimo: {self._balance}')
# se ja passou na outra validação e chegou até aqui
# entao eu tenho o valor, se completar com o limite e saldo


        # Verificação repetida
        # if value <= self.__extra_limit:
        #     self._balance += self.__extra_limit
        #     self.__extra_limit -= value
        #     ...

        print(f'\nVocê sacou: R$ -{value:.2f}')
        return checked

data_mock = ('0332', '09800-2')

mock = CheckingAccount(*data_mock)
print(mock)
# print(mock.withdraw(0))
print(mock.withdraw(5))