# Anotações sobre python sobre - Cap03 - Lesson 8 - Controle de fluxo, condições e loops

O operador ou em python é: `or`

# Anotações sobre python sobre - Cap03 - Lesson 7 - Prática print vs return


### 3 - Tomada de decisões
```
print "Example 1: Greater-than and less-than comparisons"
print 2 > 1
print 1 > 2
print 5 < 20
print 100 < 19


print "Example 2: Equality and non-equality comparisons"
print 5 == 5
print "hello" == "hello"
print 5 == 10
print 5 == '5' # what do you think will happen here?
print 7 != 10
print 7 != 7


print "Example 3: A demo of what you are about to learn"
if 3 < 5:
    print "Three is definitely smaller than 5!"

if 10 > 20: 
    print "Did you know that 10 is greater than 20!?"
else:
    print "20 is greater than 10"
```

### Sobre muitas condições
Sempre que tivermos muitas condicionais podemos criar procedures para melhorar
a legibilidade do código

```
def biggest(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c



print biggest(1, 2, 3)
#>>> 3
```
Para esse caso podemos usar uma composição de função. Pegamos o método `bigger` e
e retornamos dentro da função `biggest` passando os `argumentos`.

```
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def biggest(a, b, c):
    return bigger(bigger(a, b), c)

print biggest(1, 2, 3)
#>>> 3
```