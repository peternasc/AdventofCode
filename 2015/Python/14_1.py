import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual,"..", "Input", "14.txt")

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

def distancia(nome,velocidade,t_voando,t_parado,tempo):
    distancia = 0
    while tempo != 0:
        if tempo <= t_voando:
            distancia = tempo * velocidade + distancia
            tempo = 0
        else:
            distancia = t_voando * velocidade + distancia
            tempo = tempo - t_voando
            if tempo <= t_parado:
                tempo = 0
            else:
                tempo = tempo - t_parado

    return distancia
tempo = 2503
maior_distancia = float('-inf')
for c in linhas:
    n = c.split()
    #print(n)
    nome = str(n[0])
    velocidade = int(n[3])
    t_voando = int(n[6])
    t_parado = int(n[13])
    rena = distancia(nome,velocidade,t_voando,t_parado,tempo)
    if rena > maior_distancia:
        maior_distancia = rena
print(maior_distancia)