import os
# Obtém o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho dinâmico do arquivo dentro da pasta "Input"
caminho_arquivo = os.path.join(diretorio_atual,"..", "Input", "02.txt")

# Abre o arquivo corretamente
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

def presente(a,b,c):
    menor = 0
    a = int(a)
    b = int(b)
    c = int(c)
    if a*b < b*c and a*b < a*c:
        menor = a*b
    elif a*c < b*c and a*c < a*b:
        menor = a*c
    else:
        menor = b*c
    multiplica = (2*a*b) + (2*a*c) + (2*b*c) + menor
    return multiplica
soma = 0
for c in linhas:
    linha = c.strip()
    a,b,c = linha.split('x')
    multiplica = presente(a,b,c)
    soma += multiplica

print(soma)

