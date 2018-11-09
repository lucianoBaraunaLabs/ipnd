# Loop enquanto 2

##Separando o Problema
Primeiro precisamos compreender quais são os inputs e quais são os outputs (ou resultados) que queremos obter.

### Os inputs são:

Uma lista de 20 inteiros gerados aleatoriamente
### O output é:

Um número representando a conta do número de vezes em que o número 9 está na lista

## O Que Fazer
Portanto, queremos fazer um loop pela lista e contar quantas vezes o número 9 aparece. Se o elemento corrente é número 9, podemos aumentar a conta em 1 e mover para o próximo elemento da lista.

Vamos ver se conseguimos escrever um esboço do que fazer como se o fizéssemos manualmente, com caneta e papel:

1. Faça um loop por cada elemento da lista
2. Se o elemento é 9, aumentamos nossa conta em 
3. Já estamos no fim da lista?
4. Caso não, fazemos um loop de volta e repassamos os passos 1 a 3 while/enquanto ainda estamos passando pela lista

### Tradução
Vamos passos por esses passos e traduzi-los para código de computador.

*1.* Faça um Loop por cada elemento da lista
Parece que primeiro precisamos configurar a estrutura do loop para fazer um loop por cada elemento da lista. Para fazê-lo, devemos configurar algumas variáveis para resguardar o index corrente da lista bem como a contagem corrente:
```
index = 0
count = 0
```
Agora podemos configurar a estrutura de nosso loop:
```
while index < len(random_list):
  # Put other code here
  index = index + 1
```
Preste atenção em como já estamos adicionando index = index + 1 ao loop. Este código é crucial para garantir que o computador não entre em um loop infinito. Para a maior parte dos loops, vamos querer deixar claro e definido o ponto final. Neste caso, o ponto final é quando o número index for maior que o comprimento de nossa lista.

*2.* Se o elemento é 9, aumentamos nossa contagem em 1
Este é um exemplo clássico de cláusula `if`. Podemos acessar o elemento corrente na lista usando `random_list[index]` e então usar uma cláusula if para chegar se este elemento é 9. Pode então somar 1 caso o elemento seja igual a 9.
```
if random_list[index] == 9:
  count = count + 1
```
*3 - 4*.: Vamos fazer um loop de nossos passos caso não tenhamos alcançado o fim da lista ainda.
A construção de nosso loop já dá conta deste critério pois no topo de nosso loop, estamos sempre checando se o número index ainda é menor que o comprimento da lista aleatória: `index < len(random_list)`

Usamos a seguinte lógica: se o número index é menor que o comprimento de nossa lista, então podemos dizer seguramente que quando acessamos a lista com index, nunca criaremos um erro e seremos capazes de acessar elementos na lista com o número index.

#### Código Resposta
```
index = 0
count = 0

while index < len(random_list):
  if random_list[index] == 9:
    count = count + 1
  index = index + 1
Código Resposta Completo
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
   random_list.append(random.randint(0,10))

index = 0
count = 0

while index < len(random_list):
  if random_list[index] == 9:
    count = count + 1
  index = index + 1
```
Por favor, tenha em mente como nós já estamos adicionando `index = index + 1` o loop. Esse código é crucial para garantir que o computador não entre em um loop infinito. Para a maioria dos loops, queremos sempre definir claramente um ponto de parada. Nesse caso, o ponto de parada é quando o número indexé maior que o tamanho da nossa lista.

*2.* Se o elemento for 9, aumentamos nossa contagem em 1
Este é um exemplo clássico de uma ifdeclaração. Podemos acessar o elemento atual na lista usando `random_list[index]`e, em seguida, usar uma instrução if para verificar se o elemento é 9. Podemos incrementar a contagem em 1 se o elemento for igual a 9.
```
if random_list[index] == 9:
  count = count + 1
```
*3 - 4:* Vamos retornar aos nossos passos se ainda não tivermos chegado ao final da lista.
Nossa construção de laço já cuida desse critério, porque no topo de nosso loop, estamos sempre verificando se nosso número de índice ainda é menor que o tamanho da lista aleatória: `index < len(random_list)`

Usamos a lógica: se o número do índice for menor que o tamanho da nossa lista, podemos dizer com segurança que, sempre que acessarmos a lista index, nunca criaremos um erro e poderemos acessar elementos na lista com o número index.

#### Código de Resposta
```
index = 0
count = 0

while index < len(random_list):
  if random_list[index] == 9:
    count = count + 1
  index = index + 1
```
#### Código de resposta completa
```
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
   random_list.append(random.randint(0,10))

index = 0
count = 0

while index < len(random_list):
  if random_list[index] == 9:
    count = count + 1
  index = index + 1
```
