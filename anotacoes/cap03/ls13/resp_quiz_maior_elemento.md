Define a procedure, greatest, that takes as input a list of positive numbers, and returns the greatest number in that list. If the input list is empty, the output should be 0.
```
def greatest(list_of_numbers):
    if not list_of_numbers:
        return 0
    index = 1
    value_actual = list_of_numbers[0]
    while index < len(list_of_numbers):
        if value_actual < list_of_numbers[index]:
            value_actual = list_of_numbers[index]
        index += 1
    return value_actual

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0
```