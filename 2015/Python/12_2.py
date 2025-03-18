import json
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual,"..", "Input", "12.json")

with open(caminho_arquivo, "r", encoding="utf-8") as file:
    dados = json.load(file)

def soma_sem_red(obj):
    # Se for um inteiro, retorna o próprio número
    if isinstance(obj, int):
        return obj
    
    # Se for uma lista, soma os valores recursivamente
    if isinstance(obj, list):
        return sum(soma_sem_red(item) for item in obj)
    
    # Se for um dicionário e tiver "red" em algum valor, ignora todo o objeto
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(soma_sem_red(value) for value in obj.values())

    # Se for outro tipo (string, None, etc.), ignora e retorna 0
    return 0

# Carregar o JSON de um arquivo


# Rodando a soma sobre os dados carregados
resultado = soma_sem_red(dados)
print(resultado)