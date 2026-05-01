class cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class conta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print('depositando...', valor)

    def sacar(self, valor):
        if valor <= self.saldo + self.limite_especial:
            self.saldo -= valor
            print('sacando...', valor)
        else:
            print('saldo insuficiente:')

    def mostrar_saldo(self):
        return self.saldo

    def __str__(self):
        return f'cliente:{self.nome}\ncpf:{self.cpf}\nsaldo:{self.saldo}\nlimite:{self.limite_especial}'


class conta_premium(cliente, conta):
    def __init__(self, nome, cpf, saldo, limite_especial):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.limite_especial = limite_especial


conta1 = conta_premium('ana', 12345678909, 200, 300)
print(conta1)
print()

conta1.depositar(1000)
print('saldo atual =', conta1.saldo)
print()

conta1.sacar(400)
print('saldo atual =', conta1.saldo)
