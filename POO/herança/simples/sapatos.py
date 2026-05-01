class produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço


class tenis(produto):
    def __init__(self, nome, preço, tamanho, marca):
        self.nome = nome
        self.preço = preço
        self.tamanho = tamanho
        self.marca = marca

    def __str__(self):
        return f'produto:{self.nome}\npreço:R${self.preço:.2f}\ntamanho:{self.tamanho}\nmarca:{self.marca} '


t1 = tenis('nike air', 305.9, 38, 'nike')
t2 = tenis('adidas run', 199.9, 43, 'adidas')

print(t1)
print()
print(t2)
