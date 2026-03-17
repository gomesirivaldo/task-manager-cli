def pedir_id():

    while True:

        try:
            id_tarefa = int(input("Digite o ID da tarefa: "))
            return id_tarefa
    
        except ValueError:
            print("Por favor, digite um número válido.")