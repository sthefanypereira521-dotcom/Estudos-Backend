class Estudante:
    escola = 'ciep 130'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'nome {self.nome}\nnumero da matricula {self.matricula}\nnome da escola {self.escola}'


alunos = [
    Estudante('beatriz', 1),
    Estudante('yasmin', 2),
    Estudante('fernando', 3),
    Estudante('ana', 4)
]

for alunos in alunos:
    print(alunos, '\n')
