from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass


class Pix(Pagamento):
    def pagar(self, valor):
        print(f'pago {valor:.2f} via Pix')


class Carta_Credito(Pagamento):
    def pagar(self, valor):
        print(f'pago {valor:.2f} via cartao de credito')


Pagamento1 = Pix()
Pagamento2 = Carta_Credito()


Pagamento1.pagar(30)
Pagamento2.pagar(80)
