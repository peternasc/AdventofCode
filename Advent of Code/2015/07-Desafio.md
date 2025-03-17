# --- Dia 7: Alguma montagem necessária ---
Este ano, o Papai Noel trouxe para o pequeno Bobby Tables um conjunto de fios e portas lógicas bitwise ! Infelizmente, o pequeno Bobby está um pouco abaixo da faixa etária recomendada e precisa de ajuda para montar o circuito .

Cada fio tem um identificador (algumas letras minúsculas) e pode transportar um sinal de 16 bits (um número de 0a 65535). Um sinal é fornecido a cada fio por um gate, outro fio ou algum valor específico. Cada fio só pode obter um sinal de uma fonte, mas pode fornecer seu sinal para vários destinos. Um gate não fornece sinal até que todas as suas entradas tenham um sinal.

O livreto de instruções incluído descreve como conectar as peças: x AND y -> zsignifica conectar os fios xe ya uma porta AND e, então, conectar sua saída ao fio z.

### Por exemplo:

>123 -> xsignifica que o sinal 123é fornecido ao fio x.  
x AND y -> zsignifica que o bit a bit AND de wire xe wire yé fornecido para wire z.  
p LSHIFT 2 -> qsignifica que o valor de wire pé deslocado para a esquerda 2e então fornecido para wire q.  
NOT e -> fsignifica que o complemento bit a bit do valor de wire eé fornecido para wire f.  
Outras portas possíveis incluem OR( bitwise OR ) e RSHIFT( right-shift ). 

Se, por algum motivo, você quiser emular o circuito, quase todas as linguagens de programação (por exemplo, C , JavaScript ou Python ) fornecem operadores para essas portas.

### Por exemplo, aqui está um circuito simples:

>123 -> x  
456 -> y  
x AND y -> d  
x OR y -> e  
x LSHIFT 2 -> f  
y RSHIFT 2 -> g  
NOT x -> h  
NOT y -> i  

>Depois de executado, estes são os sinais nos fios:
d: 72  
e: 507  
f: 492  
g: 114  
h: 65412  
i: 65079  
x: 123  
y: 456 

No livreto de instruções do kit do pequeno Bobby (fornecido como entrada para o seu quebra-cabeça), qual sinal é finalmente fornecido ao fioa ?

## A resposta do seu quebra-cabeça foi 956.

# --- Parte Dois ---
Agora, pegue o sinal que você obteve em wire a, sobreponha wire bpara esse sinal e reinicie os outros wires (incluindo wire a). Qual novo sinal é finalmente fornecido para wire a?

## A resposta do seu quebra-cabeça foi 40149.