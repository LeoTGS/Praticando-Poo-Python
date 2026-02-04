class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_dados(self):
        print(f'Funcionário: {self.nome} | Salário: {self.salario}')

    def aumentar_salario(self,valor):
        self.salario = valor
        print(f'Funcionário: {self.nome} | Salário: {self.salario}')


class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        self.setor = setor
        super().__init__(nome, salario)


    def mostrar_dados(self):
        print(f'\nGerente: {self.nome} | Salário: {self.salario} | Setor: {self.setor}')
    
f1 = Funcionario('Lucas', 2000)
f1.mostrar_dados()
f1.aumentar_salario(2500)


g1 = Gerente("Leonardo", 5000, 'TI')
g1.mostrar_dados()