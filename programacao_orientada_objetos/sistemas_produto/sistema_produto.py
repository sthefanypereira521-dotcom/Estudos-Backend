from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self, nome, preço, marca):
        self.nome = nome
        self.preço = preço
        self.marca = marca

    def __str__(self):
        return f'{self.nome} custa R${self.preço:,.2f} da {self.marca}'

    def etiqueta(self):
        encomenda = f'{self.nome}'
        encomenda += f"{'.' * 7}"

        preco_formatado = f'R${self.preço:,.2f}'
        encomenda += f" {preco_formatado.center(6)}\n"

        encomenda += f"{'-' * 26}"
        encomenda += f'marca{"." * 11} -{self.marca}'

        etiqueta = Panel(encomenda, title='Produto', width=30)
        print(etiqueta)


print()
p1 = Produto('notebook', 5_990.00, 'LENOVO')
print(p1)
print()
p1.etiqueta()
print()


p2 = Produto('mouse', 130, 'RAZER')
print()
print(p2)
print()
p2.etiqueta()
