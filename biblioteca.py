class Livro():
    def __init__(self,titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = 5


    def mostrar_info(self):
        print(f"Livro: {self.titulo} | Autor: {self.autor} | Cópias Disponíveis: {self.copias}")

    def emprestar_livro(self):

        if self.copias <= 0:
            print("\nLivro Indisponível!")
            
        else:
            self.copias -= 1
            print(f"\nVocê pegou emprestado o Livro: {self.titulo}. Tem até duas semanas para devolver!")

    
    def _copias(self,novo_valor):
        print(f"\nLivro: {self.titulo} | Cópias Disponíveis: {self.copias}")
        self.copias = novo_valor
        print(f"Atualizado para {self.copias} Cópias Disponíveis! ")


class LivroEspecial(Livro):
    def __init__(self,titulo, autor, copias, status):
        self.status = status
        super().__init__(titulo, autor, copias)

    def emprestar_livro(self):
        if self.status == 'Ouro':
            return super().emprestar_livro()
        
        elif self.status == 'Prata':
            print(f"\nVocê pegou emprestado o Livro: {self.titulo}. Tem uma semana para devolver!")

        else:
            print(f"\nApenas membros de status Prata/Ouro podem pegar livros emprestados!")

        


l1 = Livro('Vida', 'Leonardo', 5)
l1.mostrar_info()
l1.emprestar_livro()
l1.emprestar_livro()
l1.emprestar_livro()
l1.emprestar_livro()
l1.emprestar_livro()
l1.emprestar_livro()

l1._copias(1)

le = LivroEspecial('Morte', 'Leonardo Segundo', 5, 'Ouro')
le.emprestar_livro()

le = LivroEspecial('Morte', 'Leonardo Segundo', 5, 'Prata')
le.emprestar_livro()

le = LivroEspecial('Morte', 'Leonardo Segundo', 5, 'Bronze')
le.emprestar_livro()


