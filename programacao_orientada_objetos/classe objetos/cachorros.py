class cachorro:
    def __init__(self, nome, cor, tamanho, peso,):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.peso = peso

    def latir(self):
        print('cachorro latindo', end=' ')
        print('woof, woof, woof')

    def brincar(self):
        print('brincando com bolinha')

    def comer(self):
        print('comendo racao')

    def __str__(self):
        return f'cachorro: nome = {self.nome} cor = {self.cor}\n tamanho = {self.tamanho} peso = {self.peso}'


cao_1 = cachorro('golden retriever', 'amarelho claro', '62cm', '37kg')

cao_1.latir()
cao_1.comer()
print()
cao_1.brincar()
cao_1.latir()
print()
print(cao_1)
