
from itertools import permutations

def verifica_valor(c1,c2,valores):
    if valores.get(c1) == None:
        return valores.get(c2)
    else:
        return valores.get(c1)

with open('09.txt','r',encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

cord = ["London to Dublin = 464",
"London to Belfast = 518",
"Dublin to Belfast = 141"]
list_dist = []
distancia = 0
valores = {}
cidades =[]
menor_distancia = []
for c in linhas:
    a,_,b,T,n = c.split()
    cidades.append(a)
    cidades.append(b)
    valores [f'{a} {b}'] = n

cid_unica = set(cidades)

combina = list(permutations(cid_unica))
dist = 0
for c in combina:
    #print(c)
    x = 0
    y = 1
    for num in range(1,len(c)):
        c1 = (f'{c[x]} {c[y]}')
        c2 = (f'{c[y]} {c[x]}')
        dist = verifica_valor(c1,c2,valores)
        #print(c1)
        #print(dist)
        x += 1
        y += 1
        list_dist.append(int(dist))
    distancia = sum(list_dist)
    menor_distancia.append(distancia)
    list_dist = []
print(min(menor_distancia))