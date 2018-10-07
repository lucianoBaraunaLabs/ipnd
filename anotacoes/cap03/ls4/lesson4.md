# Anotações sobre python sobre - Cap03 - Lesson 4 - Variáveis e Strings
## Onde manter sua atenção

`=` - significa atribuição
`"!" * 12` = aqui estamos multiplicado exclamação por 12, ex:

```
name = 'Luciano'
print 'Hello ' + name + '!' * 3 // Hello Luciano!!!
```

*No python não é permito concatenar strings com números como no javacsript*

Steings são uma sequência de caracters no phyton e elas são indexadas então com
isso nós conseguimos fazer, isso:
```
# name = "Luciano"
print name[0] #L
print name[1] #u
print name[2] #c
print name[3] #i
```

Selecionando substrings.
O operador `:` gera uma nova string apartir de uma outra.
```
name = 'Luciano'
print name[3] #i
print name[4:6] #an seleciona partir do índice 4 até 6 
print name[4:] #ano seleciona partir do índice 4 em diante
print name[:4] #Luci seleciona os valares até o limite que é 4
print name[:] #Luci seleciona tudo
```

Método `find`
Ele é utilizado para encontrar strings e retorna o posição do caracter em forma de índice. Quando não existe é retornado `-1`

```
usandoFind = "Um texto qualquer lorem"
print usandoFind.find('texto') #3
print usandoFind[3:] #texto qualquer lorem
print usandoFind.find('U') #0
print usandoFind.find('Xuxa') #-1
```
Exemplos de find em strings
```
print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]

print "Example 2: Finding substrings in a string which is stored as a variable"
my_string = "test"
print my_string.find("te")
print my_string.find("st")
print my_string[2:]

print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color # oops, this line prints out 'color: ' as well...
print favorite_color[7:] # this fixes it!

print "Example 4: Other interesting things about string.find()..."
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1  

```
No método find existe um segundo parâmetro que é utilizado como ponto de partida
para começar a busca pela string.

