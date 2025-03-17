with open('13.txt','r',encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

valores = {}
cont = 0
nomes = []

for c in linhas:
    nome1,a,feliz,valor,aa,aaa,aaaa,aaaaa,aaaaaa,aaaaaaa,n = c.split()
    nome2 = n.replace('.','')
    valor = int(valor)
    if nome1 not in nomes:
        nomes.append(nome1)

    if feliz == 'gain':
        valor = valor
    else:
        valor = valor*-1
    valores[f'{nome1} {nome2}'] = valor
   
    cont += 1
soma_felicidade = []
pessoa = ''
for c in nomes:
    maior_felicidade = 0

    for i in nomes:
        if c != i:

            proxima_pessoa = valores.get(f'{c} {i}')
            pessoa_atual = valores.get(f'{i} {c}')
            soma_dupla = proxima_pessoa + pessoa_atual

            if proxima_pessoa != None and soma_dupla > maior_felicidade:
                maior_felicidade = soma_dupla

    soma_felicidade.append(maior_felicidade)

        
print(soma_felicidade)

