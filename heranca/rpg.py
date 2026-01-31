import random

class RPG():
    def __init__(self, classe, ataque, vida, defesa):
        self.classe = classe
        self.ataque = ataque
        self.vida = vida
        self.defesa = defesa

    def bonus_defesas(self):
        bonus_de_defesa = random.choice(["ESQUIVA", "NADA", "NADA", "NADA", "NADA"])

        if bonus_de_defesa == "ESQUIVA":
            if self.quem_comeca == 1:
                print(f"\n{'-' * 20} Turno de {p1.classe} {'-' * 20}")
                print(f"{p1.classe} ATACA MAS...")
                print(f"{p2.classe} ESQUIVOU DO ATAQUE")
                self.quem_comeca = 2
            else:
                print(f"\n{'-' * 20} Turno de {p2.classe} {'-' * 20}")
                print(f"{p2.classe} ATACA MAS...")
                print(f"{p1.classe} ESQUIVOU DO ATAQUE")
                self.quem_comeca = 1
            return True
        return False

    def bonus_ataques(self):
        bonus_de_ataque = random.choice(["DANO DOBRADO", "ATAQUE NORMAL"])

        if self.quem_comeca == 1:
            print(f"\n{'-' * 20} Turno de {p1.classe} {'-' * 20}")

            if bonus_de_ataque == "DANO DOBRADO":
                dano = max(0, (p1.ataque * 2) - p2.defesa)
                p2.vida -= dano
                print(f"{p1.classe} usa DANO DOBRADO {dano} de dano")
                print(f"{p2.classe} VIDA: {p2.vida}\n")
                self.quem_comeca = 2
            else:
                dano = max(0, p1.ataque - p2.defesa)
                p2.vida -= dano
                print(f"{p1.classe} usa ATAQUE NORMAL {dano} de dano")
                print(f"{p2.classe} VIDA: {p2.vida}\n")
                self.quem_comeca = 2

        else:
            print(f"\n{'-' * 20} Turno de {p2.classe} {'-' * 20}")

            if bonus_de_ataque == "DANO DOBRADO":
                dano = max(0, (p2.ataque * 2) - p1.defesa)
                p1.vida -= dano
                print(f"{p2.classe} usa DANO DOBRADO {dano} de dano")
                print(f"{p1.classe} VIDA: {p1.vida}\n")
                self.quem_comeca = 1
            else:
                dano = max(0, p2.ataque - p1.defesa)
                p1.vida -= dano
                print(f"{p2.classe} usa ATAQUE NORMAL {dano} de dano")
                print(f"{p1.classe} VIDA: {p1.vida}\n")
                self.quem_comeca = 1

    def combate(self):
        self.quem_comeca = random.randint(1, 2)
        print(f"\n{'='*25} COMBATE INICIADO {'='*25}")

        while p1.vida > 0 and p2.vida > 0:
            if not self.bonus_defesas():
                self.bonus_ataques()

        vencedor = p1 if p1.vida > 0 else p2
        print(f"\n{vencedor.classe} VENCEU O DUELO!")


class Cavaleiro(RPG):
    def __init__(self):
        super().__init__("Cavaleiro", 20, 100, 10)

class Gladiador(RPG):
    def __init__(self):
        super().__init__("Gladiador", 25, 100, 5)

p1 = Cavaleiro()
p2 = Gladiador()
p1.combate()
