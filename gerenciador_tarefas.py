def gerenciador_tarefas():
    print("Bem-vindo ao Gerenciador de Tarefas!\n")
    tarefas = []
    while True:
        print("""\nSelecione a opção desejada:\n
1 - Adicionar Tarefa
2 - Ver Tarefas
3 - Remover Tarefa
4 - Sair\n""")
        opcao = input("Digite o número da opção desejada: ")
        if opcao.isalpha() or opcao not in ['1', '2', '3', '4']:
            print("\nErro: Digite apenas números de 1 a 4")

        match opcao:  
            case '1':
                tarefa = input("Digite o nome da tarefa: ")
                print(f"\nTarefa '{tarefa}' adicionada com sucesso!")
                tarefas.append(tarefa)
            
            case '2':
                if tarefas:
                    print("\nTarefas:")
                    for idx, tarefa in enumerate(tarefas, start=1):
                        print(f"{idx} - {tarefa}")
                
                else:
                    print("\nNenhuma tarefa cadastrada.")
            
            case '3':
                if tarefas:
                    print("\nTarefas:")
                    for idx, tarefa in enumerate(tarefas, start=1):
                        print(f"{idx} - {tarefa}")
                    num_remover = input("Digite o número da tarefa que você deseja remover: ")
                    if num_remover.isdigit() and 1 <= int(num_remover) <= len(tarefas):
                        tarefa_removida = tarefas.pop(int(num_remover) - 1)
                        print(f"\nTarefa '{tarefa_removida}' removida com sucesso!")
                    else:
                        print("\nErro: Número inválido.")
            case  '4':
                print("Obrigado por usar o Gerenciador de Tarefas!")
                break

gerenciador_tarefas()