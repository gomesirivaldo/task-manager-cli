# Gerenciador de Tarefas (CLI)

Um gerenciador de tarefas simples desenvolvido em Python para execução via terminal (CLI).

## Funcionalidades

1. Adicionar tarefas
2. Listar tarefas
3. Marcar tarefas como concluídas
4. Remover tarefas
5. Persistência de dados em arquivo JSON

## Objetivo do Projeto

Este projeto foi desenvolvido com foco em prática de fundamentos essenciais de desenvolvimento:

- Programação Orientada a Objetos (POO)
- Manipulação de arquivos com JSON
- Separação de responsabilidades (modularização)
- Estruturação de aplicações em múltiplos arquivos
- Tratamento de erros e validação de entrada

## Estrutura do Projeto

```bash
gerenciador-de-tarefas/
│
├── main.py
├── models.py
├── tarefas.py
├── arquivo.py
├── utils.py
├── README.md
└── .gitignore
```
## Tecnologias Utilizadas

- Python
- JSON
- Terminal (CLI)

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/gomesirivaldo/gerenciador-de-tarefas-cli.git
```
### 2. Acessar a pasta
 ```bash
 cd gerenciador-de-tarefas-cli
 ```

### 3. Executar o programa

```bash
python main.py
```
## Exemplo de Uso
```bash
================================
######### TASK MANAGER #########
================================
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
5 - Sair
================================
```

## Observações

- Os dados são armazenados localmente em `tarefas.json`
- Não há uso de banco de dados
- Interface baseada em terminal (CLI)

## Melhorias Futuras

- Editar tarefas
- Buscar tarefas por palavra-chave
- Filtro por status (pendente/concluída)
- Adicionar data e prioridade
- Interface web (React, Flask ou FastAPI)
- Interface gráfica (Tkinter)

## Aprendizados

Durante o desenvolvimento, foram trabalhados conceitos como:

- Conversão entre objetos e dicionários (`to_dict`/`from_dict`)
- Diferença entre dados internos e exibição (ex: `True` vs ✔)
- Manipulação de listas e estruturas de dados
- Organização de código em módulos
- Controle de fluxo e interação com usuário

## Autor

Desenvolvimento por mim como parte dos estudos em Análise e Desenvolvimento de Sistemas.

## Status

- Projeto funcional
- Possível evolução futura