
from arquivo import salvar_tarefas

def adicionar_tarefa(tarefas, proximo_id):

    descricao = input("Digite a descrição da tarefa: ")

    nova_tarefa = {
        "id": proximo_id,
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(nova_tarefa)

    salvar_tarefas(tarefas)

    print("Tarefa adicionada com sucesso!")

    return proximo_id + 1

def listar_tarefas(tarefas):

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\nLista de tarefas:")

    for tarefa in tarefas:

        status = "✔" if tarefa["concluida"] else "✘"

        print(f'{tarefa["id"]} - {tarefa["descricao"]} [{status}]')