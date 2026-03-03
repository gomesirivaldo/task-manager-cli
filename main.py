tarefas = []
proximo_id = 1

print("=== TASK MANAGER ===")
print("1 - Adicionar tarefa")
print("2 - Listar tarefas")
print("3 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    descricao = input("Digite a descrição da tarefa: ")
    
    nova_tarefa = {
        "id": proximo_id,
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    proximo_id += 1


    print("Tarefa adicionada com sucesso.")

elif opcao == "2":
    print("Lista de tarefas:")
    for tarefa in tarefas:
        status = "✔" if tarefa["Concluida"] else "✘"
        print(f'{tarefa["id"]} - {tarefa["descricao"]} [{status}]')

elif opcao == "3":
    print("Saindo...")
    
else:
    print("Opção inválida.")