import re

with open('12.txt','r',encoding='utf-8') as arq:
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