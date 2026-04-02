class Tarefa:

    def __init__(self, id, descricao, concluida=False):
        
        self.id = id
        self.descricao = descricao
        self.concluida = concluida

    def to_dict(self):

        return {
            "id": self.id,
            "descricao": self.descricao,
            "concluida": self.concluida
        }
    
    @staticmethod
    def from_dict(dados):

        return Tarefa(
            dados["id"],
            dados["descricao"],
            dados["concluida"]
        )