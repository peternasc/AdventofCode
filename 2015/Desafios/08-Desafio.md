# --- Dia 8: Fósforos ---
O espaço no trenó é limitado este ano, então o Papai Noel levará sua lista como uma cópia digital. Ele precisa saber quanto espaço ela ocupará quando armazenada.

É comum em muitas linguagens de programação fornecer uma maneira de escapar caracteres especiais em strings. Por exemplo, C , JavaScript , Perl , Python e até mesmo PHP lidam com caracteres especiais de maneiras muito semelhantes.

Entretanto, é importante perceber a diferença entre o número de caracteres na representação de código do literal de string e o número de caracteres na própria string na memória .

### Por exemplo:

>""são 2caracteres de código (as duas aspas duplas), mas a string contém zero caracteres.  
"abc"são 5caracteres de código, mas 3caracteres nos dados da string.  
"aaa\"aaa"são 10caracteres de código, mas a string em si contém seis caracteres "a" e um único caractere de aspas de escape, para um total de 7caracteres nos dados da string.  
"\x27"são 6caracteres de código, mas a string em si contém apenas um - um apóstrofo ( '), escapado usando notação hexadecimal.

Santa's list é um arquivo que contém muitas strings literais entre aspas duplas, uma em cada linha.  
As únicas sequências de escape usadas são \\(que representa uma única barra invertida), \"(que representa um caractere de aspas duplas solitário) e \xmais dois caracteres hexadecimais (que representa um único caractere com aquele código ASCII).

Desconsiderando os espaços em branco no arquivo, qual é o número de caracteres de código para literais de string menos o número de caracteres na memória para os valores das strings no total para o arquivo inteiro?

### Por exemplo 
>Dadas as quatro strings acima, o número total de caracteres do código de string ( 2 + 5 + 10 + 6 = 23) menos o número total de caracteres na memória para valores de string ( 0 + 3 + 7 + 1 = 11) é 23 - 11 = 12.

## A resposta do seu quebra-cabeça foi 1333.

# --- Parte Dois ---
Agora, vamos para o outro lado. Além de encontrar o número de caracteres do código, você deve agora codificar cada representação de código como uma nova string e encontrar o número de caracteres da nova representação codificada, incluindo as aspas duplas ao redor.

### Por exemplo:

>""codifica para "\"\"", um aumento de 2caracteres para 6.  
"abc"codifica para "\"abc\"", um aumento de 5caracteres para 9.  
"aaa\"aaa"codifica para "\"aaa\\\"aaa\"", um aumento de 10caracteres para 16.  
"\x27"codifica para "\"\\x27\"", um aumento de 6caracteres para 11.  

Sua tarefa é encontrar o número total de caracteres para representar as strings recém-codificadas menos o número de caracteres de código em cada literal de string original . 

### Por exemplo 
>Para as strings acima, o comprimento codificado total ( 6 + 9 + 16 + 11 = 42) menos os caracteres na representação de código original ( 23, assim como na primeira parte deste quebra-cabeça) é 42 - 23 = 19.

## A resposta do seu quebra-cabeça foi 2046.