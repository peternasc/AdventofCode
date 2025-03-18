from itertools import permutations
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual,"..", "Input", "13.txt")

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

valores = {}
nomes = set()

# Processar os dados do arquivo
for linha in linhas:
    partes = linha.split()
    nome1 = partes[0]
    nome2 = partes[-1].replace('.', '')
    felicidade = int(partes[3])
    if partes[2] == 'lose':
        felicidade = -felicidade

    valores[(nome1, nome2)] = felicidade
    nomes.add(nome1)
    nomes.add(nome2)

nomes = list(nomes)  # Converter para lista para gerar permutações

# Adicionando "Você" ao grupo e dando felicidade zero com todos
eu = "Você"
for nome in nomes:
    valores[(eu, nome)] = 0
    valores[(nome, eu)] = 0
nomes.append(eu)  # Adiciona "Você" à lista de nomes

# Função para calcular a felicidade de um arranjo na mesa circular
def calcular_felicidade(arranjo):
    total = 0
    for i in range(len(arranjo)):
        pessoa1 = arranjo[i]
        pessoa2 = arranjo[(i + 1) % len(arranjo)]  # A mesa é circular
        total += valores.get((pessoa1, pessoa2), 0)
        total += valores.get((pessoa2, pessoa1), 0)
    return total

# Testar todas as permutações possíveis e encontrar o melhor arranjo
melhor_felicidade = float('-inf')
melhor_arranjo = None

for perm in permutations(nomes):
    felicidade = calcular_felicidade(perm)
    if felicidade > melhor_felicidade:
        melhor_felicidade = felicidade
        melhor_arranjo = perm

# Exibir o resultado
print("Melhor disposição:", melhor_arranjo)
print("Maior felicidade total (incluindo você):", melhor_felicidade)