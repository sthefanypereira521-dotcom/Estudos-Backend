class conta:
    def __init__(self, num_agencia, cpf, saldo=0):
        self.__saldo = saldo
        self.num_agencia = num_agencia
        self.__cpf = str(cpf)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print('depositando...')

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print('sacando...')
        else:
            print(' saldo insuficiente!!! ')

    @property
    def saldo(self):
        return self.__saldo

    def mostrar_saldo(self):
        return self.__saldo

    def __str__(self):
        cpf_mask = f'{self.__cpf[:3]}***'
        return f'conta: agencia = {self.num_agencia}, cpf = {cpf_mask} saldo = {self.__saldo}'


conta = conta('0003', 68953424571, 10,)
print()

conta.mostrar_saldo()
print(conta)
print()


conta.depositar(300)
print('saldo atual =', conta.saldo)
print()


conta.sacar(150)
print('saldo atual =', conta.saldo)
print()
