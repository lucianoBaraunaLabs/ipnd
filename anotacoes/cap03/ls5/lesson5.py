# coding: utf-8

# Quiz 2
# Write Python code that prints out the number of hours in 7 weeks.

# number_hours =  24
# number_days = 7
# number_weeks = 7

# print (number_hours * number_days) * number_weeks

# Quiz 3
# s = ""
# print ('a' + s)[1:]
# print s[0] + s[1:]
# print s + ''
# print s[0:]

# # Quiz 4
# # Given the variables s and t defined as:
# s = 'udacity'
# t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

# print s[:3] + t[4:] # minha solução

# Quiz 5
# Insert the proper slicing indices for the substring variable 
# so that the slice is a string that contains everything after "A NOUN". 
# For example, if we wanted to store everything after "went", the returned 
# string would be equal to sentence[11:].

# sentence = "A NOUN went on a walk."
# substring = sentence[6:]
# print substring


# Quiz 6
# # Use string slicing to store everything before "NOUN" in substring1,
# # everything after "NOUN" and before "VERB" in substring2, and everything after "VERB" 
# # in substring3.

# sentence = "A NOUN went on a walk. It can VERB really fast."
# substring1 = sentence[:2]
# substring2 = sentence[6:30]
# substring3 = sentence[34:]

# print substring1
# print substring2
# print substring3

# Quiz 7
# Set noun_replacement and verb_replacement to your own noun and verb strings. 
# Then, concatenate the variables substring1-3, noun_replacement, and 
# verb_replacement and assign the result to the variable new_sentence so that 
# it's in the same order as the variable sentence.

# sentence = "A NOUN went on a walk. It can VERB really fast."
# substring1 = sentence[0:2]
# substring2 = sentence[6:30]
# substring3 = sentence[34:]

# noun_replacement = "MALUCO" # your noun here
# verb_replacement = "SER" # your verb here

# # # your code here
# # Meu código
# # new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3
# # print new_sentence

# # Resposta do ex
# new_sentence = ''
# new_sentence += substring1 
# new_sentence += noun_replacement
# new_sentence += substring2
# new_sentence += verb_replacement
# new_sentence += substring3
# print new_sentence

# Quiz 8
# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America. 
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# You're a spy yourself and you want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but you only know that 
# gabriel = kathleen, and kathleen = salwa, etc..

# Your mission: knowing how each alias relates to each other, assign the variables 
# gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
# the values for each alias will point to the string "Mary"

# NOTE: We can't simply assign all variables to "Mary".

# mary = "Mary"
# # Your code goes here


# # In South America, the alias Kathleen is known as the alias Gabriel, this means that:
# kathleen = mary
# gabriel = kathleen
# salwa = gabriel
# katie = salwa
# randa = katie

# # Test to see if all of these variables will print out the string "Mary"
# print gabriel
# print kathleen
# print salwa
# print katie
# print randa
# print mary

# Quiz 9
# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.
# Review Dave's video on string.find, or visit
# http://www.tutorialspoint.com/python/string_find.htm for more information.

# text = """Wow this is a fairly long body of text. Quite a few characters too.
# I wonder if the string.find method could help find where NOUN is located.
# That way, I could go out and VERB with my friends rather than counting characters
# all day long!"""

# noun_position = text.find('NOUN') #fill this in
# verb_position = text.find('VERB') #fill this in

# print noun_position
# print verb_position

# Quiz 10

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

# ENTER CODE BELOW HERE


print text[6:0].find('zip')

# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function

text = "all zip files are zipped" 
first_zip = text.find('zip')
print text.find('zip', first_zip+1)

print text.find('zip', text.find('zip')+1)