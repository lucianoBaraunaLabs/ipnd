
# Loop enquanto 1
## Separando o Problema
Primeiro precisamos compreender quis são os inputs e quais são os outputs (ou resultados) que queremos obter.

### Os inputs são:

Uma lista vazia
Uma variável que tem o valor 20, nos dizendo que queremos criar uma lista de comprimento 20
### O output é:

A lista de inteiros aleatórios entre 0 e 10 pode parecer com algo assim:
```
[7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
```

## O Que Fazer
Portanto queremos gerar uma lista de inteiros aleatórios dada uma lista vazia. Um jeito é usar o método append() para listas e adicionar um inteiro aleatório, 20 vezes.

Esta é a forma como uma pessoa faria isso manualmente com papel e caneta. Vamos ver se conseguimos escrever um esboço do que fazer como se o fizéssemos manualmente, com caneta e papel:

1. Gere um inteiro aleatório entre 0 e 10
2. Adicione este inteiro aleatório à nossa lista
3. Já temos uma lista de comprimento 20?
4. Caso não, nós fazemos um loop e refazemos os passos 1 a 3 while/enquanto o comprimento da lista é menor que 20

Se fôssemos traduzir estes passos para código real, usaríamos um while loop que checa se o comprimento da lista é menos que 20.

#### Código Resposta
```
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
   random_list.append(random.randint(0,10))
Aqui está o código alternativo que simplifica um pouco esta lógica se o código acima for difícil de compreender. import random

random_list = []
list_length = 20
count = 0

while count < list_length:
   random_list.append(random.randint(0,10))
   count += 1
```