
# coding: utf-8
# Quiz 4 - Mediana
# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.
# https://pt.wikipedia.org/wiki/Mediana_%28estat%C3%ADstica%29
# Make sure your procedure has a return statement.

# def bigger(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# def biggest(a,b,c):
#     return bigger(a,bigger(b,c))
    
# def median(a, b, c): # Checa a média de valor entre os números
#     big = biggest(a,b,c)
#     if big == a:
#         return bigger(b, c)
#     if big == b:
#         return bigger(a, c)
#     else:
#         return bigger(a, b)


# print(median(1,2,2))
# #>>> 2

# print(median(9,3,6))
# #>>> 6

# print(median(7,8,7))
# #>>> 7

#Quiz 5
# Write code for the function random_noun, which takes in no inputs but outputs 
# one of two nouns randomly. Use the randint function to generate a number 
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1. 
# Feel free to experiment with different nouns, but for submission purposes return 
# the string "sofa" if the number is 0, else return "llama".

from random import randint

def random_noun():
    # your code here
    sort_value = randint(0, 1)
    if sort_value == 0:
        return "sofa"
    else:
        return "llama"
    
print random_noun()





