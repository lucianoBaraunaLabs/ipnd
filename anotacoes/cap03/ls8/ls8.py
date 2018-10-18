
# coding: utf-8
# Quiz 6
# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

# def is_friend(name):
#     if name[0] == 'D':
#         return True
#     elif name[0] == 'N':
#         return True
#     else:
#         return False


# print is_friend('Diane')
# #>>> True

# print is_friend('Ned')
# #>>> True

# print is_friend('Moe');
# #>>> False

#Quiz 9
# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

# Minha solução
# def biggest(num1, num2, num3):
#     if num1 > num2:
#         if num1 > num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2 > num3:
#             return num2
#         else:
#             return num3

# def biggest(a,b,c):
#     if a > b:
#         if a > c:
#             return a
#         else:
#             return c
#     else:
#         if b > c:
#             return b
#         else:
#             return c



# print biggest(1, 2, 3)
# #>>> 3

# print biggest(1, 3, 2)

# print biggest(3, 1, 2)

# def remove_spaces(text):
#     text_without_spaces = '' #empty string for now
#     while text != '':
#         next_character = text[0]
#         if next_character != ' ':    #that's a single space
#             text_without_spaces = text_without_spaces + next_character
#         text = text[1:]
#     return text_without_spaces
# print remove_spaces("hello my name is andy how are you?")

# Quiz 16
# def print_numbers(n):
#     i = 1
#     while i < n:
#         i += 1
#         print i

# print_numbers(3)