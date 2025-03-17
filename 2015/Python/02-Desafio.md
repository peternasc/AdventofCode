# --- Dia 2: Disseram-me que não haveria matemática ---
Os elfos estão ficando sem papel de embrulho, então eles precisam enviar um pedido de mais. Eles têm uma lista das dimensões (comprimento l, largura we altura h) de cada presente, e querem pedir apenas exatamente a quantidade que precisam.

Felizmente, cada presente é uma caixa (um prisma retangular reto perfeito ), o que torna o cálculo do papel de embrulho necessário para cada presente um pouco mais fácil: encontre a área da superfície da caixa, que é 2*l*w + 2*w*h + 2*h*l. Os elfos também precisam de um pouco mais de papel para cada presente: a área do menor lado.

### Por exemplo:

>Um presente com dimensões 2x3x4requer 2*6 + 2*12 + 2*8 = 52metros quadrados de papel de embrulho mais 6metros quadrados de folga, totalizando 58metros quadrados.  
Um presente com dimensões 1x1x10requer 2*1 + 2*10 + 2*10 = 42metros quadrados de papel de embrulho mais 1metros quadrados de folga, totalizando 43metros quadrados.  
Todos os números na lista dos elfos estão em pés . Quantos pés quadrados totais de papel de embrulho eles devem pedir?

## A resposta do seu quebra-cabeça foi **1586300**.

# --- Parte Dois ---
Os elfos também estão ficando sem fita. As fitas são todas da mesma largura, então eles só precisam se preocupar com o comprimento que precisam pedir, o que eles gostariam que fosse exato.

A fita necessária para embrulhar um presente é a menor distância ao redor de seus lados, ou o menor perímetro de qualquer face. Cada presente também requer um laço feito de fita; os pés de fita necessários para o laço perfeito são iguais aos pés cúbicos de volume do presente. Mas não pergunte como eles amarram o laço; eles nunca dirão.

### Por exemplo:

>Um presente com dimensões 2x3x4requer 2+2+3+3 = 1030 cm de fita para embrulhar o presente, mais 2*3*4 = 2430 cm de fita para o laço, totalizando 3430 cm.  
Um presente com dimensões 1x1x10requer 1+1+1+1 = 430 cm de fita para embrulhar o presente, mais 1*1*10 = 1030 cm de fita para o laço, totalizando 1430 cm.  
Quantos metros totais de fita eles devem encomendar?

## A resposta do seu quebra-cabeça foi **3737498**.