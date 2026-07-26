class Livro:
    biblioteca = 'biblioteca municipal'

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f'nome do livro {self.titulo}\nnome do autor(ª) {self.autor}\n{self.biblioteca}'


livros = [
    Livro('harry potter', 'j.k'),
    Livro('percy jackson', 'rick riordan'),
    Livro('the vampire diaries', 'L.J. Smith')
]

for livros in livros:
    print(livros, '\n')
