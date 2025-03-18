import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual,"..", "Input", "08.txt")

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

barras = 0
aspas = 0
linha_nova = 0
soma_novo = 0
soma_carac = 0

for c in linhas:
    b = c.count('\\')
    a = c.count('\"')
    x = c.strip()
    linha_nova = b + a + 2 + len(x)
    soma_novo += linha_nova

for c in linhas:
    a = (len(c) - 1)
    soma_carac += a

soma_carac += 1

print(soma_novo - soma_carac)