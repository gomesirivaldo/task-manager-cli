
from arquivo import salvar_tarefas

def buscar_tarefa_por_id(tarefas, id_tarefas):

    for tarefa in tarefas:

        if tarefa["id"] == id_tarefas:
            return tarefa
    
    return None

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

def concluir_tarefa(tarefas):
    id_tarefa = int(input("Digite o ID da tarefa para concluir: "))

    for tarefa in tarefas:

        if tarefa["id"] == id_tarefa:

            tarefa["concluida"] = True

            salvar_tarefas(tarefas)

            print("Tarefa concluída com sucesso.")
            return
    
    print("Tarefa não encontrada.")

def remover_tarefa(tarefas):

    id_tarefa = int(input("Digite o ID da tarefa para remover: "))

    for tarefa in tarefas:

        if tarefa["id"] == id_tarefa:

            tarefas.remove(tarefa)

            salvar_tarefas(tarefas)

            print("Tarefa removida com sucesso.")
            return
    
    print("Tarefa não encontrada.")