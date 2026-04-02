import json
from models import Tarefa

def carregar_tarefas():
    
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            return [Tarefa.from_dict(t) for t in dados]
    
    except FileNotFoundError:
        return[]
    
    except json.JSONDecodeError:
        print("Arquivo JSON inválido ou vazio. Reiniciando dados...")
        return []
    
def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            [t.to_dict() for t in tarefas], 
            arquivo, 
            ensure_ascii=False,
            indent=4
        )