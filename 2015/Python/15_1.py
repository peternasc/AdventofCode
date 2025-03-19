import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual,"..", "Input", "15.txt")

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

valor = 10 # valor que é a soma total dos numeros 

#Logica para passar por todos os valores possiveis sempra somando 100
for a in range (1,valor):
    for b in range(1,valor-a):
        for c in range (1,valor - a - b):
            d = valor - a -b - c
            print(a,b,c,d)

