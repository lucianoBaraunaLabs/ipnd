# Loop enquanto 4

## Quebrando o problema
Vamos primeiro identificar quais são as entradas e quais são as saídas (ou resultados) que queremos obter.

### As entradas são:

Uma lista de números inteiros que representam a distribuição de todos os números que ocorreram em uma lista gerada aleatoriamente

### A saída é:

Uma tabela bem formatada que mostra o número e sua contagem correspondente assim:
```
  number | occurrence
       0 | 1
       1 | 2
       2 | 3
       3 | 2
       4 | 2
       5 | 1
       6 | 1
       7 | 2
       8 | 3
       9 | 1
      10 | 2
```
## O que fazer
Primeiro precisamos entender que ainda precisamos percorrer todos os elementos em count_list e simplesmente imprimir o índice e o valor de count_list em um formato específico.

Vamos ver se podemos escrever um esboço do que fazer se fizermos isso manualmente em caneta e papel:

1. Imprimir o cabeçalho "número | ocorrência"
2. Fazer um loop por cada elemento na lista gerada aleatoriamente
3. Imprima o número de espaços necessários para obter o alinhamento correto desejado
4. Obtenha o índice atual e seu valor associado em nossa lista
5. Imprimir índice e valor neste formato: "índice | valor"
6. Estamos no final do ciclo?
7. Se não, voltamos e passamos pelas etapas 1 a 5 novamente enquanto ainda estamos passando pela lista

### Tradução
Vamos percorrer essas etapas e traduzir essas etapas em código de computador.

*1.* Imprima o cabeçalho "número | ocorrência"
Isso é direto:
```
print "number | occurrence"
```

*2.* Faça um loop por cada elemento na lista gerada aleatoriamente. Portanto, configuramos nossa estrutura de loop.
```
index = 0

while index < len(random_list):
  # Put other code here
  index = index + 1
```
Por favor, tenha em mente como nós já estamos adicionando index = index + 1o loop. Esse código é crucial para garantir que o computador não entre em um loop infinito. Para a maioria dos loops, queremos sempre definir claramente um ponto de parada. Nesse caso, o ponto de parada é quando o número indexé maior que o tamanho da nossa lista.

*3.* Imprima o número de espaços necessários para obter o alinhamento correto desejado.
Para fazer isso dinamicamente, precisamos perceber que podemos calcular o número de espaços em branco necessários para imprimir antes de imprimir nosso índice. Se quisermos imprimir a string "0", precisamos perceber que precisamos imprimir 5 espaços antes de imprimir "0", a fim de alinhar com a letra r em "número" no cabeçalho.

O que acontece se decidirmos imprimir a string "10?" Precisamos imprimir 4 espaços porque os caracteres "10" ocupam 2 espaços. Independentemente do número, a quantidade total de espaços e caracteres deve somar 6, o tamanho da string "number".

Portanto, em cada loop, calculamos dinamicamente o número de espaços que precisamos imprimir, dependendo do tamanho dos caracteres de cada índice:
```
num_spaces = len("number") - len(str(index))
```
Como len ("number") nunca muda para cada iteração de loop, vamos calcular e armazenar o tamanho da string "number" fora do loop:
```
num_len = len("number")
while index < len(count_list):
  num_spaces = num_len - len(str(index))
```
*4-5.* Obtenha o índice atual e seu valor associado em nossa lista e imprima-o no formato desejado. Nós convertemos nossos inteiros em string e usamos o operador "+" para concatenar nossas strings.
```
print " " * num_spaces + str(index) + " | " + str(count_list[index])
```
*5:* Estamos no final do loop? Se não, nós fazemos um loop de volta e passamos as instruções while loop novamente.
Nossa construção de laço já cuida desse critério, porque no topo de nosso loop, estamos sempre verificando se nosso número de índice ainda é menor que o tamanho da lista aleatória:index < len(random_list)

Usamos a lógica: se o número do índice for menor que o tamanho da nossa lista, podemos dizer com segurança que, sempre que acessarmos a lista index, nunca criaremos um erro e poderemos acessar elementos na lista com o número index.

#### Código de Resposta
```
print "number | occurrence"
index = 0
num_len = len("number")

while index < len(count_list):
  num_spaces = num_len - len(str(index))
  print " " * num_spaces + str(index) + " | " + str(count_list[index])
  index = index + 1
Código de resposta completa
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1

print "number | occurrence"
index = 0
num_len = len("number")

while index < len(count_list):
  num_spaces = num_len - len(str(index))
  print " " * num_spaces + str(index) + " | " + str(count_list[index])
  index = index + 1
```