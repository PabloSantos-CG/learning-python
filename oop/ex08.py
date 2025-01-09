from enum import Enum, auto

class Payment(Enum):
    PRAZO = auto()
    BOLETO = auto()
    CREDITO = auto()
    DEBITO = auto()

# Payment_Secundary = Enum('Payment', ['PRAZO', 'BOLETO', 'CREDITO', 'DEBITO'])
# Payment_Secundary = Enum('Payment', ('PRAZO', 'BOLETO', 'CREDITO', 'DEBITO'))
Payment_Secundary = Enum('Payment_', {'PRAZO', 'BOLETO', 'CREDITO', 'DEBITO'})
print(Payment_Secundary.DEBITO)
