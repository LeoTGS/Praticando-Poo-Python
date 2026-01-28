import random

class Personagem():
    def __init__(self, classe, nome):
        self.classe = classe
        self.nome = nome

        if classe == "Cavaleiro":
            self.vida = 100
            self.forca = 20
            self.defesa = 13

        elif classe == "Guerreiro":
            self.vida = 100
            self.forca = 25
            self.defesa = 8

        else:
            self.vida = random.randint(70,110)
            self.forca = random.randint(5,35)
            self.defesa = random.randint(1,15)


    def combate(self, p1, p2):
        quem_começa = random.randint(1,2)
        print(f"Quem começa o combate: {p1.nome if quem_começa == 1 else p2.nome}\n")
        while p1.vida > 0 and p2.vida > 0:

            if quem_começa == 1:

                dano = p1.forca + random.randint(5,10) - p2.defesa
                dano = max(0, dano)
                p2.vida -= dano
                print(f"\n{p1.nome}: Causou {dano} em {p2.nome}!\nVida atual do {p2.nome}: {p2.vida}")
                
                quem_começa = 2
            else:

                dano = p2.forca + random.randint(5,10) - p1.defesa
                dano = max(0,dano)
                p1.vida -= dano
                print(f"\n{p2.nome}: Causou {dano} em {p1.nome}!\nVida atual do {p1.nome}: {p1.vida}")

                quem_começa = 1
        
        if p1.vida <= 0:
            print(f"\n{p1.nome} foi derrotado! {p2.nome} Venceu!")
        
        else:
            print(f"\n{p2.nome} foi derrotado! {p1.nome} Venceu!")
        
        print("\n----- Fim do Combate -----")




p1 = Personagem("Cavaleiro", "Leonardo")
p2 = Personagem("Guerreiro", "João")

p1.combate(p1,p2)