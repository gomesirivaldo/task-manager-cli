import json

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def gerar_proximo_id(tarefas):
    if not tarefas:
        return 1
    return max(tarefa["id"] for tarefa in tarefas) + 1

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")

    nova_tarefa = {
        "id": gerar_proximo_id(tarefas),
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa adicionada com sucesso.\n")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa adicionada.\n")
        return 
    
    print("\nLista de tarefas: ")
    for tarefa in tarefas:
        status = "✔" if tarefa["concluida"] else "✘"
        print(f'{tarefa["id"]} - {tarefa["descricao"]} [{status}]')
    print()

def main():
    tarefas = carregar_tarefas()

    while True:
        print("=== TASK MANAGER ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida.\n")

if __name__=="__main__":
    main()