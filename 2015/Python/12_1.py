import re
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual,"..", "Input", "12.txt")
with open(caminho_arquivo, "r", encoding="utf-8") as arq:
    arquivo = arq.read()


def soma_numeros(texto):
    padrao = r'(-?\d+)'
    encontra = re.findall(padrao,texto)
    lista = []
    for c in encontra:
        lista.append(int(c))
    return sum(lista)

t = soma_numeros(arquivo)
print(t)