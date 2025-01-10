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

data_mock = ('0332', '09800-2')

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

        if balance_plus_limit or balance_plus_limit == 0:
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
            f"\nAgência: {self._agency}; Conta: {self._number_account}"
            f"\nSaldo: {self.balance:.2f};"
            f"\n{
                f'Limite extra: {self._CheckingAccount__extra_limit}'
                if hasattr(self, '_CheckingAccount__extra_limit') else ''
            }"
            f"\n"
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

# mock_ = SavingsAccount(*data_mock)
# print(mock_)

class CheckingAccount(Account):
    def __init__(self, agency, number_account):
        super().__init__(agency, number_account)
        self.__extra_limit = 300

    def withdraw(self, value):
        balance_plus_limit = self.balance + self.__extra_limit

        checked = self.validate_withdrawal_amount(value, balance_plus_limit)
        if not checked[0]:
            return checked

        if value <= self._balance:
            self._balance -= value
            print(f'Você sacou: R$ -{value:.2f}')
            return checked

        required_value = value - self.balance
        self.__extra_limit -= required_value

        if self.balance > 0:
            self._balance = 0

        print(f'\nVocê sacou: R$ -{value:.2f}')
        return checked


mock = CheckingAccount(*data_mock)
print(mock)

mock.deposit(1200)
print(mock)

# mock.withdraw(200)
# print(mock)

print(mock.withdraw(1500))
print(mock)

# print(mock.withdraw(100))
# print(mock)

print(mock.withdraw(10))
print(mock)