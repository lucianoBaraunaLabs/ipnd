
 Define a procedure, product_list, that takes as input a list of numbers,and returns a number that is the result of multiplying all those numbers together.

```
#Minha resposta
def product_list(list_of_numbers):
    acumalated = 1
    for target_item in list_of_numbers:
        acumalated *= target_item
    return acumalated 
s
print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1
```

