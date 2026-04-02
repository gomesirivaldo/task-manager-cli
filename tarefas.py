
from arquivo import salvar_tarefas
from utils import pedir_id
from models import Tarefa

def buscar_tarefa_por_id(tarefas, id_tarefas):

    for tarefa in tarefas:

        if tarefa.id == id_tarefas:
            return tarefa
    
    return None

def adicionar_tarefa(tarefas, proximo_id):

    descricao = input("Digite a descrição da tarefa: ")

    nova_tarefa = Tarefa(proximo_id, descricao)

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

        status = "✔" if tarefa.concluida else "✘"

        print(f'{tarefa.id} - {tarefa.descricao} [{status}]')

def concluir_tarefa(tarefas):

    id_tarefa = pedir_id()

    tarefa = buscar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa:

        tarefa.concluida = True
        salvar_tarefas(tarefas)

        print("Tarefa concluída com sucesso.")
    
    else:
        print("Tarefa não encontrada.")

def remover_tarefa(tarefas):

    id_tarefa = pedir_id()

    tarefa = buscar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa:

        tarefas.remove(tarefa)
        salvar_tarefas(tarefas)

        print("Tarefa removida com sucesso.")

    else:
        print("Tarefa não encontrada.")

def obter_proximo_id(tarefas):

    if len(tarefas) == 0:
        return 1
    
    maior_id = 0

    for tarefa in tarefas:
        if tarefa.id > maior_id:
            maior_id = tarefa.id
    
    return maior_id + 1