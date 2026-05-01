class produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço


class alimento(produto):
    def __init__(self, nome, preço, validade):
        super().__init__(nome, preço)
        self.validade = validade

    def aplicar_desconto(self, porcentagem):
        self.preço -= self.preço * (porcentagem / 100)

    def __str__(self):
        return f'produto: {self.nome}\npreço: R${self.preço:.2f}\nvalidade: {self.validade}'


alimento1 = alimento('feijão 2k', 8.0, '10/05/2028')
print(alimento1)
print()

alimento2 = alimento('arroz 2k', 6.0, '31/06/2029')
print(alimento2)
print()

alimento3 = alimento('peito de frango 1k', 21, '01/06/2026')
alimento3.aplicar_desconto(10)
print(alimento3)
