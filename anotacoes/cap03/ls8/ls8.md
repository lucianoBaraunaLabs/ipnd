# Anotações sobre python sobre - Cap03 - Lesson 8 - Controle de fluxo, condições e loops

O operador ou em python é: `or`

Semrpre que tivermos muitas condicionais podemos criar procedures para melhorar
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