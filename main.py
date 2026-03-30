from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa, obter_proximo_id
from arquivo import carregar_tarefas
from utils import mostrar_menu, limpar_tela, pausar

def main():

    tarefas = carregar_tarefas()

    proximo_id = obter_proximo_id(tarefas)

    while True:

        limpar_tela()
        mostrar_menu()
        
        opcao = input("Escolha uma opção: ")

        print("________________________________")
        if opcao == "1":
            proximo_id= adicionar_tarefa(tarefas, proximo_id)
            pausar()

        elif opcao == "2":
            listar_tarefas(tarefas)
            pausar()

        elif opcao == "3":
            concluir_tarefa(tarefas)
            pausar()

        elif opcao == "4":
            remover_tarefa(tarefas)
            pausar()

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.\n")

if __name__=="__main__":
    main()