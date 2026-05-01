class produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço


class estoque:
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def repor(self, qnt):
        self.quantidade += qnt
        print('repondo... camisas')
        print(qnt, camiseta.nome)


class camisa(produto, estoque):
    def __init__(self, nome, preço, quantidade, tamanho, marca, cor):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade
        self.tamanho = tamanho
        self.marca = marca
        self.cor = cor

    def __str__(self):
        return (
            f'produto:{self.nome}\n'
            f'preço:R${self.preço:.2f}\n'
            f'quatidade:{self.quantidade}\n'
            f'tamanho:{self.tamanho}\n'
            f'marca:{self.marca}\n'
            f'cor:{self.cor}'
        )


camiseta = camisa('nike ', 305.9, 10, 'M, GG',
                  'nike', 'preto, branco, vermelho')
blusa = camisa('puma', 199.9, 5, 'M, G, P, GG', 'puma', 'branco com preto')

print(camiseta)
print()
print(blusa)
print()

camiseta.repor(2)
