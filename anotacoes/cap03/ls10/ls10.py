
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

# from random import randint

# def random_noun():
#     # your code here
#     sort_value = randint(0, 1)
#     if sort_value == 0:
#         return "sofa"
#     else:
#         return "llama"
    
# print random_noun()


# Quiz 8 Transformador de palavras

# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word. 

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

# Minha resposta
# def word_transformer(word):
#     if word == 'NOUN':
#         return random_noun()
#     elif word == 'VERB':
#         return random_verb()
#     else:
#         return word[0]

# print word_transformer('XUXA')

# Quiz 8 Processando Mad Libs
# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

# from random import randint

# def random_verb():
#     random_num = randint(0, 1)
#     if random_num == 0:
#         return "run"
#     else:
#         return "kayak"
        
# def random_noun():
#     random_num = randint(0,1)
#     if random_num == 0:
#         return "sofa"
#     else:
#         return "llama"

# def word_transformer(word):
#     if word == "NOUN":
#         return random_noun()
#     elif word == "VERB":
#         return random_verb()
#     else:
#         return word[0]
        
# def process_madlib(mad_lib):
#     processed = ""
#     processed = mad_lib.replace("NOUN",word_transformer("NOUN"))
#     processed = processed.replace("VERB",word_transformer("VERB"))
#     return processed 
    
# test_string_1 = "This is a good NOUN to use when you VERB your food"
# test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
# print process_madlib(test_string_1)
# print process_madlib(test_string_2)


    


