# Loop enquanto 3
## Separando o Problema
Vamos primeiro identificar quais são os inputs e quais são os outputs (ou resultados) que queremos obter.

### Os inputs são:

Uma lista de 20 inteiros gerados aleatoriamente
### O output é:

Uma lista de inteiros na qual cada número (vamos chamar de "n") representa a conta de um inteiro que ocorre um n número de vezes na lista de inteiros gerada aleatoriamente.

Por exemplo, se o número 4 está na lista gerada aleatoriamente 5 vezes, então teremos outra lista que contém o número 5 em index 4 nesta lista. Se o número 6 está na lista gerada aleatoriamente 2 vezes, então nossa lista output terá o número 2 em index 6 desta lista. O output até então ficaria assim: `[0,0,0,0,5,0,2,0,0,0,0]`

## O que Fazer
Vamos ver se conseguimos escrever um esboço do que fazer como se o fizéssemos manualmente, com caneta e papel:

1. Faça um loop por cada elemento na lista gerada aleatoriamente
2. Obtenha o número corrente em nossa lista
3. Precisamos, agora, somar um à nossa conta para este número
4. Vamos obter a conta corrente deste número checando nossa lista output e então soma um à esta conta
5. Chegamos no fim de nosso loop?
6. Caso não, fazemos um loop de voltar e passamos novamente pelos passos de 1 a 5while/enquanto ainda estamos passando pela lista

### Tradução
Vamos passar por esses passos e traduzi-los em código de computador.

*1.* Faça um loop por cada elemento na lista
Parece que primeiro precisamos configurar a estrutura do loop para cada elemento da lista. Para fazê-lo, devemos configurar algumas variáveis para resguardar o index corrente da lista e criar a lista de contagem inicial (initial count_list):
```
count_list = [0]*11
index = 0
```
Agora podemos configurar a estrutura de nosso loop:
```
while index < len(random_list):
  # Put other code here
  index = index + 1
```
Tenha em mente que já estamos adicionando index = index + 1 ao loop. Este código é crucial para garantir que o computador não entre em um loop infinito. Para a maior parte dos loops, vamos querer deixar claro e definido o ponto final. Neste caso, o ponto final é quando o número index for maior que o comprimento de nossa lista.

*2.* Obtenha o número corrente em nossa lista
Obtemos o número acessando a lista com o index corrente:
```
number = random_list[index]
```
*3-4:* Agora somamos um à nossa contagem para este número.
Uma vez que o index de count_list servirá como nosso ponto de consulta, podemos soma à nossa contagem do número corrente assim:
```
count_list[number] = count_list[number] + 1
```
*5:* Chegamos no fim de nosso loop? Caso contrário, fazemos um loop e passamos um loop while pelas instruções novamente.
A construção de nosso loop já dá conta deste critério pois no topo de nosso loop, estamos sempre checando se o número index ainda é menor que o comprimento da lista aleatória: `index < len(random_list)`

Usamos a seguinte lógica: se o número index é menor que o comprimento de nossa lista, então podemos dizer seguramente que quando acessamos a lista com `index`, nunca criaremos um erro e seremos capazes de acessar elementos na lista com o número `index`.

#### Código Resposta
```
count_list = [0]*11
count = 0

while index < len(random_list):
  number = random_list[index]
  count_list[number] = count_list[number] + 1
  index = index + 1
```
#### Código Resposta Completo
```
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0
count = 0

while index < len(random_list):
  number = random_list[index]
  count_list[number] = count_list[number] + 1
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