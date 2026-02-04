class Animal():
    def __init__(self, nome, idade):
        self._nome  = nome
        self._idade = idade


    def get_nome(self):
        return self._nome
    
    def set_nome(self,novo_nome):
        if novo_nome != '':
            self._nome = novo_nome
        
        else:
            print("O nome não pode ser vazio!")
    
    def get_idade(self):
        return self._idade
    
    def set_idade(self,nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        
        else:
            print("A idade não pode ser negativa!")
        
    
    def mostrar_info(self):
        print(f"\nNome: {self._nome} | Idade: {self._idade}")

class Peixe(Animal):
    def __init__(self,nome, idade, tipo_agua):
        super().__init__(nome, idade)
        self._tipo_agua = tipo_agua

    def nadar(self):
        print(f"O peixe {self._nome} está nadando!\n")

    def mostrar_info(self):
        print(f"\nPeixe: {self._nome} | Idade: {self._idade} | Tipo de Agua: {self._tipo_agua}")

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self._raca = raca

    def miar(self):
        print(f" O gato {self._nome} está miando!")

    def mostrar_info(self):
        print(f"\nGato: {self._nome} | Idade: {self._idade} | Raça: {self._raca}")
    

c = Animal("Luke", 3 )
c.mostrar_info()

p = Peixe("Dori", 3, 'Doce')
p.mostrar_info()
p.nadar()

g = Gato("Bila", 2, 'Caramela')

g.mostrar_info()
g.miar()
