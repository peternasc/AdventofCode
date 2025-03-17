from collections import Counter


with open('14.txt', 'r', encoding='utf-8') as arquivo:
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
vitoriosos = []
vitoria = {}
for i in range(1,tempo+1):
    for c in linhas:
        n = c.split()
        nome = str(n[0])
        velocidade = int(n[3])
        t_voando = int(n[6])
        t_parado = int(n[13])
        dist = distancia(nome,velocidade,t_voando,t_parado,i)
        vitoria[nome] = dist
    maior = max(vitoria.values())
    for c in vitoria.items():
        if c[1] == maior:
            vitoriosos.append(c[0])

lista_pontos = Counter(vitoriosos)
campeao = max(lista_pontos.values())
print(campeao)