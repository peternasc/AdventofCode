import string as st
import re


def alfa():
    n = st.ascii_lowercase
    a = []
    for c in n:
        if c not in 'iol':
            a.append(c)
    return "".join(a)

#Gerar sequencia de 3 letrar consecutivas para utilizar no padrao de pesquisa 
'''
n = alfa()
lista = []
for c in range(0,len(n) - 2):
    item = f'{n[c]}{n[c+1]}{n[c+2]}'
    lista.append(item)
a = '|'.join(lista)
print(a)
'''

def dupla(text):
    padrao = r'(\w)\1'
    dupla = re.findall(padrao,text)
    if len(set(dupla)) < 2:             
        return False
    alfabeto = st.ascii_lowercase

    for i in range(len(dupla) - 1):
        if abs(alfabeto.index(dupla[i]) - alfabeto.index(dupla[i + 1])) == 1:
            return False 
    
    return True
    


def tres_carac(text):
    padrao = r'abc|bcd|cde|def|efg|fgh|ghj|hjk|jkm|kmn|mnp|npq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz'
    tres = re.findall(padrao,text)
    if len(tres) > 0:
        return True
    else:
        return False
    
def sem_iol(text):
    lista = []
    s = 'iol'
    for c in s:
        if c in text:
            lista.append(False)
        else:
            lista.append(True)

    if False in lista:
        return False
    else:
        return True


alfabeto = st.ascii_lowercase
senha = list('hxbxxyzz')


while ''.join(senha) != 'z'*len(senha):
    for c in range(len(senha) -1,-1,-1):
        indice_atual = alfabeto.index(senha[c])
       
        if senha[c] != 'z':
            senha[c] = alfabeto[indice_atual + 1]
            break
        else:
            senha[c] = 'a'
    
    nova_senha = ''.join(senha)
    if dupla(nova_senha) and tres_carac(nova_senha) and sem_iol(nova_senha):
        print(nova_senha)
        break
