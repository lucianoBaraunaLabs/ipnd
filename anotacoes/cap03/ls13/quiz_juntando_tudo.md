 Write code for the function play_game, which takes in as inputs parts_of_speech (a list of acceptable replacement words) and ml_string (a string that  can contain replacement words that are found in parts_of_speech). Your play_game function should return the joined list replaced, which will have the same structure as ml_string, only that replacement words are swapped out with "corgi", since this program cannot replace those words with user input. 

```
def play_game(ml_string, parts_of_speech):    
    replaced = []
    # your code here
    string_list = ml_string.split( )
    # Meu código
    # Quando encontra virgula ele não respeita ela. O código do certo corrige esse
    # erro.
    # index = 0
    # while index < len(string_list):
    #     if word_in_pos(string_list[index], parts_of_speech):
    #         string_list[index] = "corgi"

    #     replaced.append(string_list[index])
    #     index += 1
    
    # return ' '.join(replaced)
    # Codigo do curso
    for word in string_list:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            # resolve o erro de acentuação aqui com o replace
            word = word.replace(replacement, 'CORG') 
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_game(test_string, parts_of_speech)
```