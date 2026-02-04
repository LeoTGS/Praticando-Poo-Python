class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    
    def apresentacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos")

class Aluno(Pessoa):
    def __init__(self,nome, idade, matricula):
        self.matricula = matricula
        super().__init__(nome, idade)

    def apresentacao_aluno(self):
        print(f'\nMeu nome é {self.nome} e eu estou na faculdade')

    def estudar(self):
        print(f'\n{self.nome} está estudando!')
    

p1 = Pessoa('Leonardo', 23)
p1.apresentacao()

p1_aluno = Aluno('Leonardo', 23, 'Sim')
p1_aluno.apresentacao_aluno()
p1_aluno.estudar()