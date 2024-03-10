class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def calcularmedia(self):
        return (self.nota1 + self.nota2)/2

aluno1 = Aluno('igor', 8.5, 7.0)
mediaaluno1 = aluno1.calcularmedia()
print(f'Média do aluno {aluno1.nome}: {mediaaluno1}')
