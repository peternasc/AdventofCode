# --- Dia 5: Ele não tem elfos internos para isso? ---
O Papai Noel precisa de ajuda para descobrir quais sequências em seu arquivo de texto são boas ou más.

Uma boa string é aquela com todas as seguintes propriedades:

Ele contém pelo menos três vogais ( aeiouapenas), como aei, xazegov, ou aeiouaeiouaeiou.
Ele contém pelo menos uma letra que aparece duas vezes seguidas, como xx, abcdde( dd), ou aabbccdd( aa, bb, cc, ou dd).
Ele não contém as strings ab, cd, pq, ou xy, mesmo que elas façam parte de um dos outros requisitos.
### Por exemplo:

>ugknbfddgicrmopné bom porque tem pelo menos três vogais ( u...i...o...), uma letra dupla ( ...dd...) e nenhuma das substrings não permitidas.  
aaaé legal porque tem pelo menos três vogais e uma letra dupla, mesmo que as letras usadas por regras diferentes se sobreponham.  
jchzalrnumimnmhpé travesso porque não tem nenhuma letra dupla.
haegwjzuvuyypxyué travesso porque contém a string xy.  
dvszwmarrgswjxmbé travesso porque contém apenas uma vogal.  

Quantas cordas são boas?

## A resposta do seu quebra-cabeça foi 255.

# --- Parte Dois ---
Percebendo o erro de seus caminhos, Santa mudou para um modelo melhor de determinar se uma corda é travessa ou boazinha. Nenhuma das regras antigas se aplica, pois todas são claramente ridículas.

Agora, uma boa string é aquela com todas as seguintes propriedades:

Ele contém um par de quaisquer duas letras que aparecem pelo menos duas vezes na sequência sem se sobrepor, como xyxy( xy) ou aabcdefgaa( aa), mas não como aaa( aa, mas se sobrepõe).
Ele contém pelo menos uma letra que se repete com exatamente uma letra entre elas, como xyx, abcdefeghi( efe), ou mesmo aaa.
### Por exemplo:

>qjhvhtzxzqqjkmpbé legal porque tem um par que aparece duas vezes ( qj) e uma letra que se repete com exatamente uma letra entre elas ( zxz).  
xxyxxé legal porque tem um par que aparece duas vezes e uma letra que se repete com uma entre elas, mesmo que as letras usadas por cada regra se sobreponham.  
uurcxstgmygtbstgé travesso porque tem um par ( tg) mas não se repete com uma única letra entre eles.  
ieodomkazucvgmuyé travesso porque tem uma letra repetida com uma entre ( odo), mas nenhum par que aparece duas vezes.  

Quantas strings são permitidas com essas novas regras?

## A resposta do seu quebra-cabeça foi 55.