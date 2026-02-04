class Pai():
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade   

    
    def mostrar_info(self):
        print(f"\nNome do Cachorro: {self._nome}\nIdade: {self._idade}")

    def get_nome(self):
        return self._nome
    
    def set_nome(self, novo_nome):
        if novo_nome != '':
            self._nome = novo_nome
            
        else:
            print(f"O nome não pode ser 'vazio' ")

        
    def get_idade(self):
        return self._idade
    
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        
        else:
            print(f"A idade não pode ser menor que 0")


class Cao(Pai):
    def __init__(self, nome, idade, raca):
        super().__init__(nome,idade)
        self._raca = raca

    
    def latir(self):
        print("\nAU AU AU")

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Raca: {self._raca}")



c = Cao("Luke", 3, "PitMonster")
c.mostrar_info()
c.latir()

c.set_nome("Mike")
c.set_idade(8)
c.mostrar_info()



