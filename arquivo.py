import json

def carregar_tarefas():
    
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    
    except FileNotFoundError:
        return[]
    
def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)