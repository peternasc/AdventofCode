import os
import re

def mult(x,y):
    return x * y

def somarListas(a,b,c,d):
    item1 = a[0] + b[0] + c [0] + d[0]
    item2 = a[1] + b[1] + c [1] + d[1]
    item3 = a[2] + b[2] + c [2] + d[2]
    item4 = a[3] + b[3] + c [3] + d[3]
    mult = item1*item2*item3*item4
    if mult <= 0:
        mult = 0
    return mult


diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual,"..", "Input", "15.txt")

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

padrao = r'.\d'
aux = 1

for c in linhas:
    teste = re.findall(padrao,c)
    if aux == 1:
        i1 = teste
    if aux == 2:
        i2 = teste
    if aux == 3:
        i3 = teste
    else:
        i4 = teste
    aux += 1

item1 = list(map(int,i1))
item2 = list(map(int,i2))
item3 = list(map(int,i3))
item4 = list(map(int,i4))


#print(item1)
#print(item2)
#print(item3)
#print(item4)

valor = 100 # valor que é a soma total dos numeros 


maior = 0

#Logica para passar por todos os valores possiveis sempra somando 100
for a in range (1,valor):
    for b in range(1,valor-a):
        for c in range (1,valor - a - b):
            d = valor - a -b - c
            #print(a,b,c,d)
            lista1 = list(map(mult, item1, [a] * len(item1)))
            lista2 = list(map(mult, item2, [b] * len(item2)))
            lista3 = list(map(mult, item3, [c] * len(item3)))
            lista4 = list(map(mult, item4, [d] * len(item4)))
            #print(lista1,lista2,lista3,lista4)
            soma = somarListas(lista1,lista2,lista3,lista4)
            #print(soma)
            if soma > maior:
                maior = soma
print(maior)





