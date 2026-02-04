import random
import time


class RPG:
    def __init__(self, classe, vida, ataque, defesa):
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def status(self):
        print(f"{self.classe} | Vida: {self.vida} | Ataque: {self.ataque} | Defesa: {self.defesa}")

    def bonus_defesa(self):
        bonus = random.choice(["ESQUIVA", "NADA", "NADA", "NADA"])
        if bonus == "ESQUIVA":
            print(f"{self.classe} ESQUIVOU!!!")
            return True
        return False

    def atacar(self, defensor):

        print(f"{self.classe} ATACA!")

        if defensor.bonus_defesa():
            return

        bonus = random.choice(["DOBRO", "NADA", "NADA"])

        if bonus == "DOBRO":
            dano = max(0, self.ataque * 2 - defensor.defesa)
            print(f"{self.classe} ACERTA ATAQUE DANO EM DOBRO ({dano})")
        else:
            dano = max(0, self.ataque - defensor.defesa)
            print(f"{self.classe} ACERTA ATAQUE NORMAL ({dano})")

        defensor.vida -= dano
        print(f"VIDA DO {defensor.classe.upper()}: {defensor.vida}")

    def combate(self, p2):
        atacante, defensor = (self, p2) if random.randint(1, 2) == 1 else (p2, self)

        print(f"{'='*15} {atacante.classe} começa o combate! {'='*15}\n")

        while self.vida > 0 and p2.vida > 0:
            atacante.atacar(defensor)
            print()
            time.sleep(2)


            atacante, defensor = defensor, atacante


        if self.vida <= 0:
            print(f"{p2.classe} venceu o combate!")
        else:
            print(f"{self.classe} venceu o combate!")


class Cavaleiro(RPG):
    def __init__(self):
        super().__init__(classe="Cavaleiro", vida=100, ataque=20, defesa=10)


class Gladiador(RPG):
    def __init__(self):
        super().__init__(classe="Gladiador", vida=100, ataque=25, defesa=5)


player1 = Cavaleiro()
player2 = Gladiador()

player1.combate(player2)
