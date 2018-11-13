# -*- coding: utf-8 -*-


# def greatest(list_of_numbers):
#     if not list_of_numbers:
#         return 0
#     index = 1
#     value_actual = list_of_numbers[0]
#     while index < len(list_of_numbers):
#         if value_actual < list_of_numbers[index]:
#             value_actual = list_of_numbers[index]
#         index += 1
#     return value_actual

# print greatest([4,23,1])
# #>>> 23
# print greatest([])
# #>>> 0

string1 = "Yesterday, PERSON and I went to the PLACE. On our way, we saw a ADJECTIVE NOUN on a bike."
string2 = "PLACE is located on the ADVERB side of Dublin, near the mainly ADJECTIVE areas of PLACE."
list_of_words1 = string1.split(' ')
list_of_words2 = string1.split(',')

print list_of_words1
print list_of_words2
