# -*- coding: utf-8 -*-


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