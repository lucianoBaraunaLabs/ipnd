# -*- coding: utf-8 -*-

# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 


# Escreva o código para a função play_game, que aceita como entradas parts_of_speech
# (uma lista de palavras de substituição aceitáveis) e ml_string (uma string que
# pode conter palavras de substituição que são encontradas em parts_of_speech). Seu play_game
# função deve retornar a lista unida substituída, que terá a mesma estrutura
# como ml_string, apenas as palavras de substituição são trocadas por "corgi", já que
# programa não pode substituir essas palavras pela entrada do usuário.

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced = ['casa', 'carro']
    # your code here
    string_list = ml_string.split( )
    if word_in_pos(string_list[2], parts_of_speech):
        string_list[2] = "corgi"
    
    return ' '.join(string_list)
    
    
    
print play_game(test_string, parts_of_speech)  