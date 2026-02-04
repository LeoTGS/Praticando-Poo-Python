veiculos = []

while True:
    print("Sistema de Veículos")
    print("""
1 - Criar Carro
2 - Criar Moto
3 - Lista de Veículos
4 - Interagir com Veículo
5 - Sair""")




    opcao = int(input("Selecione a opção desejada: "))




    match opcao:
            case  1:
                marca  = str(input("\nDigite a marca do carro: "))

                modelo = input("Digite o modelo: ")

                ano = int(input("Digite o ano: "))

                veiculos.append(f"Marca: {marca} | Modelo: {modelo} | Ano: {ano}")

            case  2:
                marca  = str(input("\nDigite a marca do carro: "))

                modelo = input("Digite o modelo: ")

                ano = int(input("Digite o ano: "))

                veiculos.append(f"Marca: {marca} | Modelo: {modelo} | Ano: {ano}")


    for ind, name in enumerate(veiculos, 1):
        print(ind, name)