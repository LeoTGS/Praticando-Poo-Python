class Conta():
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def mostrar_dados(self):
        print(f"Titular: {self._titular} | Saldo: {self._saldo}")

    def depositar_valor(self, valor):

        if valor <= 0:
            print("\nValor Negado!")

        else:
            self._saldo += valor
            print(f"\nDepósito de R$ {valor} adicionados com sucesso!")

    def sacar(self,valor):
        
        if valor > self._saldo or valor <= 0:
            print(f"\nValor Negado!")

        else:
            self._saldo -= valor
            print(f"\nVocê sacou R$ {valor}  com sucesso!")

    def get_saldo(self):
        print(f"Seu saldo: R$ {self._saldo}")

    def set_saldo(self, novo_valor):

        if novo_valor >= 0:
            self._saldo = novo_valor
            print(f"\nSaldo atualizado para R$ {self._saldo}")

        else:
            print(f"\nValor Negado!")
            
    
c1 = Conta('Leonardo', 1000)

c1.mostrar_dados()
c1.depositar_valor(1000)
c1.get_saldo()

c1.sacar(1500)
c1.get_saldo()

c1.set_saldo(-1)
