class animal:
    def __init__(self, num_patas, cor, peso):
        self.num_patas = num_patas
        self.cor = cor
        self.peso = peso

    def __str__(self):
        return f'animal: num_patas = {self.num_patas}, cor = {self.cor}, peso = {self.peso}:'


class mamifero(animal):
    def __init__(self, num_patas, cor, peso):
        self.cor = cor
        self.peso = peso
        super().__init__(num_patas, cor, peso)


class ave(animal):
    def __init__(self, num_patas, cor, peso):
        self.cor = cor
        self.peso = peso
        super().__init__(num_patas, cor, peso)


class cachorro(mamifero):
    pass


class gato(mamifero):
    pass


class leao(mamifero):
    pass


class ornitorrinco(mamifero, ave):
    pass


cachorro = cachorro(4, 'preto e branco', '25kg')
print(cachorro, 'cachorro')
print()

ornitorrinco = ornitorrinco(4, 'verde', '2kg')
print(ornitorrinco, 'ornitorrinco')
print()

gato = gato(4, 'laranjinha', '4kg')
print(gato, 'gato')
print()

leao = leao(4, 'marrom-claro', '130kg')
print(leao, 'leao')
print()
