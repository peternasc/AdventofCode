# --- Dia 15: Ciência para Pessoas Famintas ---
Hoje, você se propôs a aperfeiçoar sua receita de biscoito de leite. Tudo o que você precisa fazer é encontrar o equilíbrio certo de ingredientes.

Sua receita deixa espaço para exatamente 100colheres de chá de ingredientes. Você faz uma lista dos ingredientes restantes que você poderia usar para terminar a receita (sua entrada de quebra-cabeça) e suas propriedades por colher de chá :

capacity(o quão bem isso ajuda o biscoito a absorver o leite)
durability(quão bem ele mantém o biscoito intacto quando cheio de leite)
flavor(como fica gostoso o biscoito)
texture(como melhora a sensação do biscoito)
calories(quantas calorias ele adiciona ao biscoito)
Você só pode medir ingredientes em quantidades de colheres de chá inteiras com precisão, e você tem que ser preciso para que possa reproduzir seus resultados no futuro. A pontuação total de um cookie pode ser encontrada somando cada uma das propriedades (totais negativos se tornam 0) e então multiplicando tudo junto, exceto calorias.

### Por exemplo, suponha que você tenha estes dois ingredientes :

>Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8  
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3  
Então, escolher usar 44colheres de chá de caramelo e 56colheres de chá de canela (porque as quantidades de cada ingrediente devem somar 100) resultaria em um biscoito com as seguintes propriedades:  
Um capacityde44*-1 + 56*2 = 68  
Um durabilityde44*-2 + 56*3 = 80  
Um flavorde44*6 + 56*-2 = 152  
Um texturede44*3 + 56*-1 = 76  
Multiplicando-os juntos ( 68 * 80 * 152 * 76, ignorando caloriespor enquanto) resulta em uma pontuação total de 62842880, que por acaso é a melhor pontuação possível dados esses ingredientes. Se alguma propriedade tivesse produzido um total negativo, ele teria se tornado zero, fazendo com que a pontuação inteira se multiplicasse para zero.

Considerando os ingredientes da sua cozinha e suas propriedades, qual é a pontuação total do biscoito com maior pontuação que você consegue fazer?