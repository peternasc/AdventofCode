# --- Dia 6: Provavelmente um risco de incêndio ---
Como seus vizinhos continuam derrotando você no concurso de decoração de casa de fim de ano ano após ano, você decidiu instalar um milhão de luzes em uma grade de 1000x1000 .

Além disso, como você foi especialmente gentil este ano, o Papai Noel lhe enviou instruções sobre como exibir a configuração de iluminação ideal.

As luzes na sua grade são numeradas de 0 a 999 em cada direção; as luzes em cada canto estão em 0,0, 0,999, 999,999, e 999,0. As instruções incluem se turn on, turn off, ou togglevários intervalos inclusivos fornecidos como pares de coordenadas. Cada par de coordenadas representa cantos opostos de um retângulo, inclusive; um par de coordenadas como 0,0 through 2,2portanto se refere a 9 luzes em um quadrado 3x3. Todas as luzes começam desligadas.

Para derrotar seus vizinhos este ano, tudo o que você precisa fazer é instalar suas luzes seguindo as instruções que o Papai Noel lhe enviou.

### Por exemplo:

>turn on 0,0 through 999,999 acenderia (ou deixaria acesas) todas as luzes.  
toggle 0,0 through 999,0 alternaria a primeira linha de 1000 luzes, desligando as que estavam acesas e ligando as que estavam apagadas.  
turn off 499,499 through 500,500 desligaria (ou deixaria apagadas) as quatro luzes do meio.  

Depois de seguir as instruções, quantas luzes são acesas ?

## A resposta do seu quebra-cabeça foi 377891.

# --- Parte Dois ---
Você acabou de implementar seu padrão de luz vencedor quando percebe que traduziu errado a mensagem do Papai Noel do antigo élfico nórdico.

A grade de luz que você comprou na verdade tem controles de brilho individuais; cada luz pode ter um brilho de zero ou mais. Todas as luzes começam em zero.

A frase turn onna verdade significa que você deve aumentar o brilho dessas luzes em 1.

A frase turn offna verdade significa que você deve diminuir o brilho dessas luzes em 1, até um mínimo de zero.

A frase togglena verdade significa que você deve aumentar o brilho dessas luzes em 2.

Qual é o brilho total de todas as luzes combinadas depois de seguir as instruções do Papai Noel?

### Por exemplo:

>turn on 0,0 through 0,0 aumentaria o brilho total em 1.  
toggle 0,0 through 999,999 aumentaria o brilho total em 2000000.
## A resposta do seu quebra-cabeça foi 14110788.