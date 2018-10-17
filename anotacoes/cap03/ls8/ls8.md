# Anotações sobre python sobre - Cap03 - Lesson 8 - Controle de fluxo, condições e loops

O operador ou em python é: `or`

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