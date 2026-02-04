import time

class Veiculos():
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    def mostrar_info(self):
        print(f"Marca: {self._marca} | Veículo: {self._modelo} | Marca: {self._marca} | Ano: {self.ano}")
    
    def get_marca(self):
        self._marca

    def set_marca(self, nova_marca):
        if nova_marca != '':
            self._marca = nova_marca

        else:
            print("A marca não pode ser vazia")

    def get_modelo(self):
        self._modelo

    def set_modelo(self, nova_modelo):
        if nova_modelo != '':
            self._modelo = nova_modelo

        else:
            print("O modelo não pode ser vazio")

    def get_ano(self):
        self._ano

    def set_ano(self, novo_ano):
        if novo_ano != '':
            self._ano = novo_ano

        else:
            print("O Ano não pode ser vazio")
    

class Carro():
    def __init__(self, marca, modelo, ano, tipo_combustivel):
        super().__init__(marca, modelo, ano)
        self._tipo_combustivel = tipo_combustivel

    def mostrar_info(self):
        super().mostrar_info()

    def tipo_combustivel(self):
        self._tipo_combustivel()
    
    
    def ligar_motor(self):
        print("Motor ligado")


class Moto():
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self._cilindradas = cilindradas

    def mostrar_info(self):
        super().mostrar_info()
    
    def empinar(self):
        print("Empinando Moto")

veiculos = []
print("Sistema de Veículos")
while True:

    print("""
1 - Criar Carro
2 - Criar Moto
3 - Lista de Veículos
4 - Interagir com Veículo
5 - Sair""")
    
    opcao = int(input("\nSelecione a opção desejada: "))

    match opcao:
        case  1:
            marca  = str(input("\nDigite a marca do carro: "))
            if not marca.isalpha(): 
                print("Digite apenas letras")
                continue

                

            modelo = input("Digite o modelo: ")

            ano = int(input("Digite o ano: "))

            veiculos.append(f"Marca: {marca} | Modelo: {modelo} | Ano: {ano}")


        case 2:
            marca  = str(input("\nDigite a marca da moto: "))

            modelo = input("Digite o modelo: ")

            ano = int(input("Digite o ano: "))

            veiculos.append(f"Marca: {marca} | Modelo: {modelo} | Ano: {ano}")
        
        case 3:
            print("\nVeiculos:")
            for ind, vei in enumerate(veiculos, 1):
                print(f"{ind} - {vei}")

        case 4:
            print("\nVeículos para interagir")
            print("""
        
1 - Carro
2 - Moto""")
            veiculo = int(input("Selecione a opção que deseja: "))
            
            match veiculo:
                case 1:
                    print("\nMotor ligando...")
                    time.sleep(1.5)
                    print("VRUM VRUM VRUM")

                case 2:
                    print("Chamando no Grauuuuu!")

        case 5:
            print("Obrigado e até mais!")
            break
                    



            
