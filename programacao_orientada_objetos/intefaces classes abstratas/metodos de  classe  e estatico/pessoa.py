class pessoa:
    @staticmethod
    def maior_idade(idade):
        if idade >= 18:
            return 'maior idade'
        return 'menor idade'


print(pessoa.maior_idade(18))
print(pessoa.maior_idade(16))
